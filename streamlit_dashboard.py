"""
Research Opportunities Interactive Dashboard
Streamlit application for exploring funding opportunities with advanced filtering
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from pathlib import Path
from datetime import datetime
import re

# Page configuration
st.set_page_config(
    page_title="Research Opportunities Explorer",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .filter-section {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and cache the dataset"""
    csv_path = '/mnt/user-data/outputs/research_opportunities_merged.csv'
    
    if not Path(csv_path).exists():
        return None, "Dataset not found. Please run merge_batches.py first!"
    
    try:
        df = pd.read_csv(csv_path, encoding='utf-8', quoting=1)
        
        # Parse deadline dates
        deadline_cols = [col for col in df.columns if 'deadline' in col.lower()]
        for col in deadline_cols:
            try:
                df[f'{col}_parsed'] = pd.to_datetime(df[col], errors='coerce')
            except:
                pass
        
        # Convert funding amounts to numeric
        for col in ['funding_amount_min', 'funding_amount_max', 'funding_amount_avg']:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Parse duration to numeric (extract years/months)
        if 'duration' in df.columns:
            df['duration_numeric'] = df['duration'].apply(extract_duration_numeric)
        
        return df, None
    except Exception as e:
        return None, f"Error loading dataset: {str(e)}"

def extract_duration_numeric(duration_str):
    """Extract numeric duration from string (in months)"""
    if pd.isna(duration_str):
        return None
    
    duration_str = str(duration_str).lower()
    
    # Extract years
    years_match = re.search(r'(\d+)\s*year', duration_str)
    years = int(years_match.group(1)) if years_match else 0
    
    # Extract months
    months_match = re.search(r'(\d+)\s*month', duration_str)
    months = int(months_match.group(1)) if months_match else 0
    
    total_months = (years * 12) + months
    return total_months if total_months > 0 else None

def create_metric_cards(df):
    """Display key metrics in cards"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="🎓 Total Opportunities",
            value=f"{len(df):,}"
        )
    
    with col2:
        unique_countries = df['country'].nunique() if 'country' in df.columns else 0
        st.metric(
            label="🌍 Countries",
            value=f"{unique_countries}"
        )
    
    with col3:
        if 'funding_amount_avg' in df.columns:
            avg_funding = df['funding_amount_avg'].median()
            st.metric(
                label="💰 Median Funding",
                value=f"${avg_funding:,.0f}" if pd.notna(avg_funding) else "N/A"
            )
        else:
            st.metric(label="💰 Median Funding", value="N/A")
    
    with col4:
        unique_types = df['opportunity_type'].nunique() if 'opportunity_type' in df.columns else 0
        st.metric(
            label="📋 Opportunity Types",
            value=f"{unique_types}"
        )

def apply_filters(df):
    """Apply sidebar filters to the dataset"""
    st.sidebar.markdown("## 🔍 Filters")
    
    filtered_df = df.copy()
    
    # Location filter
    if 'country' in df.columns:
        st.sidebar.markdown("### 🌍 Location")
        countries = ['All'] + sorted(df['country'].dropna().unique().tolist())
        selected_country = st.sidebar.selectbox("Country", countries)
        
        if selected_country != 'All':
            filtered_df = filtered_df[filtered_df['country'] == selected_country]
    
    # Region filter
    if 'region' in df.columns:
        regions = ['All'] + sorted(df['region'].dropna().unique().tolist())
        selected_region = st.sidebar.selectbox("Region", regions)
        
        if selected_region != 'All':
            filtered_df = filtered_df[filtered_df['region'] == selected_region]
    
    # Duration filter
    st.sidebar.markdown("### ⏱️ Duration")
    if 'duration_numeric' in filtered_df.columns:
        duration_values = filtered_df['duration_numeric'].dropna()
        if len(duration_values) > 0:
            min_dur, max_dur = int(duration_values.min()), int(duration_values.max())
            
            duration_range = st.sidebar.slider(
                "Duration (months)",
                min_value=min_dur,
                max_value=max_dur,
                value=(min_dur, max_dur)
            )
            
            filtered_df = filtered_df[
                (filtered_df['duration_numeric'].isna()) |
                ((filtered_df['duration_numeric'] >= duration_range[0]) &
                 (filtered_df['duration_numeric'] <= duration_range[1]))
            ]
    
    # Funding amount filter
    st.sidebar.markdown("### 💰 Funding Amount")
    funding_col = None
    for col in ['funding_amount_avg', 'funding_amount_min', 'funding_amount_max']:
        if col in filtered_df.columns:
            funding_col = col
            break
    
    if funding_col:
        funding_values = filtered_df[funding_col].dropna()
        if len(funding_values) > 0:
            min_fund = int(funding_values.min())
            max_fund = int(funding_values.max())
            
            funding_range = st.sidebar.slider(
                "Funding Amount (USD)",
                min_value=min_fund,
                max_value=max_fund,
                value=(min_fund, max_fund),
                step=1000,
                format="$%d"
            )
            
            filtered_df = filtered_df[
                (filtered_df[funding_col].isna()) |
                ((filtered_df[funding_col] >= funding_range[0]) &
                 (filtered_df[funding_col] <= funding_range[1]))
            ]
    
    # Field of study filter
    if 'field_of_study' in df.columns:
        st.sidebar.markdown("### 📚 Field of Study")
        fields = ['All'] + sorted(df['field_of_study'].dropna().unique().tolist())
        selected_field = st.sidebar.selectbox("Field", fields)
        
        if selected_field != 'All':
            filtered_df = filtered_df[filtered_df['field_of_study'] == selected_field]
    
    # Career stage filter
    if 'career_stage' in df.columns:
        st.sidebar.markdown("### 👨‍🎓 Career Stage")
        stages = ['All'] + sorted(df['career_stage'].dropna().unique().tolist())
        selected_stage = st.sidebar.selectbox("Career Stage", stages)
        
        if selected_stage != 'All':
            filtered_df = filtered_df[filtered_df['career_stage'] == selected_stage]
    
    # Opportunity type filter
    if 'opportunity_type' in df.columns:
        st.sidebar.markdown("### 📋 Opportunity Type")
        types = ['All'] + sorted(df['opportunity_type'].dropna().unique().tolist())
        selected_type = st.sidebar.selectbox("Type", types)
        
        if selected_type != 'All':
            filtered_df = filtered_df[filtered_df['opportunity_type'] == selected_type]
    
    # Deadline filter
    st.sidebar.markdown("### 📅 Deadline")
    deadline_filter = st.sidebar.radio(
        "Show deadlines",
        ["All", "Upcoming (2026)", "Past deadlines", "No deadline info"]
    )
    
    if deadline_filter != "All":
        deadline_col = None
        for col in filtered_df.columns:
            if 'deadline' in col.lower() and '_parsed' in col:
                deadline_col = col
                break
        
        if deadline_col:
            if deadline_filter == "Upcoming (2026)":
                filtered_df = filtered_df[
                    (filtered_df[deadline_col] >= datetime.now()) &
                    (filtered_df[deadline_col].dt.year == 2026)
                ]
            elif deadline_filter == "Past deadlines":
                filtered_df = filtered_df[filtered_df[deadline_col] < datetime.now()]
            elif deadline_filter == "No deadline info":
                filtered_df = filtered_df[filtered_df[deadline_col].isna()]
    
    # Display active filters count
    num_filters = 0
    if selected_country != 'All': num_filters += 1
    if 'selected_region' in locals() and selected_region != 'All': num_filters += 1
    if selected_field != 'All': num_filters += 1
    if 'selected_stage' in locals() and selected_stage != 'All': num_filters += 1
    if 'selected_type' in locals() and selected_type != 'All': num_filters += 1
    if deadline_filter != "All": num_filters += 1
    
    st.sidebar.markdown("---")
    st.sidebar.info(f"🔍 **{num_filters}** active filters\n\n📊 **{len(filtered_df):,}** opportunities match")
    
    # Reset filters button
    if st.sidebar.button("🔄 Reset All Filters"):
        st.rerun()
    
    return filtered_df

def create_visualizations(df):
    """Create interactive visualizations"""
    
    # Geographic distribution
    st.markdown("### 🌍 Geographic Distribution")
    col1, col2 = st.columns(2)
    
    with col1:
        if 'country' in df.columns:
            country_counts = df['country'].value_counts().head(15).reset_index()
            country_counts.columns = ['Country', 'Count']
            
            fig = px.bar(
                country_counts,
                x='Count',
                y='Country',
                orientation='h',
                title="Top 15 Countries",
                color='Count',
                color_continuous_scale='Blues'
            )
            fig.update_layout(height=500, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        if 'region' in df.columns:
            region_counts = df['region'].value_counts().reset_index()
            region_counts.columns = ['Region', 'Count']
            
            fig = px.pie(
                region_counts,
                values='Count',
                names='Region',
                title="Regional Distribution",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
    
    # Funding and opportunity analysis
    st.markdown("### 💰 Funding & Opportunities")
    col1, col2 = st.columns(2)
    
    with col1:
        if 'opportunity_type' in df.columns:
            type_counts = df['opportunity_type'].value_counts().reset_index()
            type_counts.columns = ['Type', 'Count']
            
            fig = px.bar(
                type_counts,
                x='Type',
                y='Count',
                title="Opportunity Types",
                color='Count',
                color_continuous_scale='Viridis'
            )
            fig.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        if 'funding_amount_avg' in df.columns:
            funding_data = df[df['funding_amount_avg'].notna()].copy()
            if len(funding_data) > 0:
                fig = px.histogram(
                    funding_data,
                    x='funding_amount_avg',
                    nbins=30,
                    title="Funding Amount Distribution",
                    labels={'funding_amount_avg': 'Funding Amount (USD)'},
                    color_discrete_sequence=['#ff7f0e']
                )
                fig.update_layout(height=400, showlegend=False)
                st.plotly_chart(fig, use_container_width=True)
    
    # Career stage and field analysis
    st.markdown("### 🎓 Career Stage & Field Analysis")
    col1, col2 = st.columns(2)
    
    with col1:
        if 'career_stage' in df.columns:
            stage_counts = df['career_stage'].value_counts().reset_index()
            stage_counts.columns = ['Career Stage', 'Count']
            
            fig = px.bar(
                stage_counts,
                x='Count',
                y='Career Stage',
                orientation='h',
                title="Career Stage Distribution",
                color='Count',
                color_continuous_scale='Purples'
            )
            fig.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        if 'field_of_study' in df.columns:
            field_counts = df['field_of_study'].value_counts().head(10).reset_index()
            field_counts.columns = ['Field', 'Count']
            
            fig = px.pie(
                field_counts,
                values='Count',
                names='Field',
                title="Top 10 Fields of Study",
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    # Timeline analysis
    st.markdown("### 📅 Deadline Timeline")
    deadline_col = None
    for col in df.columns:
        if 'deadline' in col.lower() and '_parsed' in col:
            deadline_col = col
            break
    
    if deadline_col:
        deadline_data = df[df[deadline_col].notna()].copy()
        if len(deadline_data) > 0:
            deadline_data['Month'] = deadline_data[deadline_col].dt.month
            deadline_data['Year'] = deadline_data[deadline_col].dt.year
            
            monthly_counts = deadline_data.groupby(['Year', 'Month']).size().reset_index(name='Count')
            
            fig = px.line(
                monthly_counts,
                x='Month',
                y='Count',
                color='Year',
                title="Application Deadlines by Month",
                labels={'Month': 'Month', 'Count': 'Number of Deadlines'},
                markers=True
            )
            fig.update_xaxes(
                tickmode='array',
                tickvals=list(range(1, 13)),
                ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    # Competitiveness analysis
    if 'acceptance_rate_category' in df.columns:
        st.markdown("### 🎯 Competitiveness Analysis")
        
        comp_counts = df['acceptance_rate_category'].value_counts().reset_index()
        comp_counts.columns = ['Category', 'Count']
        
        fig = px.pie(
            comp_counts,
            values='Count',
            names='Category',
            title="Acceptance Rate Categories",
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

def display_data_table(df):
    """Display interactive data table"""
    st.markdown("### 📊 Detailed Opportunities Table")
    
    # Select columns to display
    display_cols = []
    for col in ['opportunity_id', 'program_name', 'institution', 'country', 
                'opportunity_type', 'funding_amount_avg', 'duration', 
                'deadline_primary', 'career_stage', 'field_of_study', 'application_url']:
        if col in df.columns:
            display_cols.append(col)
    
    if display_cols:
        # Display dataframe with formatting
        display_df = df[display_cols].copy()
        
        # Format funding amounts
        if 'funding_amount_avg' in display_df.columns:
            display_df['funding_amount_avg'] = display_df['funding_amount_avg'].apply(
                lambda x: f"${x:,.0f}" if pd.notna(x) else "N/A"
            )
        
        # Make URLs clickable
        if 'application_url' in display_df.columns:
            display_df['application_url'] = display_df['application_url'].apply(
                lambda x: f'<a href="{x}" target="_blank">Apply</a>' if pd.notna(x) else ""
            )
        
        # Display with pagination
        st.dataframe(
            display_df,
            use_container_width=True,
            height=600,
            hide_index=True
        )
        
        # Download button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Filtered Data (CSV)",
            data=csv,
            file_name=f"filtered_opportunities_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )

def display_opportunity_details(df):
    """Display individual opportunity details"""
    st.markdown("### 🔍 Opportunity Details")
    
    if 'program_name' in df.columns and len(df) > 0:
        program_names = df['program_name'].dropna().tolist()
        
        selected_program = st.selectbox(
            "Select a program to view details:",
            options=["Select..."] + program_names
        )
        
        if selected_program != "Select...":
            opportunity = df[df['program_name'] == selected_program].iloc[0]
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**🎓 Program:** {opportunity.get('program_name', 'N/A')}")
                st.markdown(f"**🏛️ Institution:** {opportunity.get('institution', 'N/A')}")
                st.markdown(f"**🌍 Country:** {opportunity.get('country', 'N/A')}")
                st.markdown(f"**📋 Type:** {opportunity.get('opportunity_type', 'N/A')}")
                st.markdown(f"**👨‍🎓 Career Stage:** {opportunity.get('career_stage', 'N/A')}")
                st.markdown(f"**📚 Field:** {opportunity.get('field_of_study', 'N/A')}")
            
            with col2:
                if 'funding_amount_avg' in opportunity and pd.notna(opportunity['funding_amount_avg']):
                    st.markdown(f"**💰 Funding:** ${opportunity['funding_amount_avg']:,.0f}")
                st.markdown(f"**⏱️ Duration:** {opportunity.get('duration', 'N/A')}")
                st.markdown(f"**📅 Deadline:** {opportunity.get('deadline_primary', 'N/A')}")
                st.markdown(f"**🎯 Acceptance Rate:** {opportunity.get('acceptance_rate_category', 'N/A')}")
                
                if 'application_url' in opportunity and pd.notna(opportunity['application_url']):
                    st.markdown(f"**🔗 Application:** [Apply Here]({opportunity['application_url']})")
            
            # Description
            if 'description' in opportunity and pd.notna(opportunity['description']):
                st.markdown("**📝 Description:**")
                st.info(opportunity['description'])
            
            # Eligibility
            if 'eligibility_criteria' in opportunity and pd.notna(opportunity['eligibility_criteria']):
                st.markdown("**✅ Eligibility:**")
                st.success(opportunity['eligibility_criteria'])

def main():
    """Main application function"""
    
    # Header
    st.markdown('<p class="main-header">🎓 Research Opportunities Explorer</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Discover and Filter Global Funding Opportunities</p>', unsafe_allow_html=True)
    
    # Load data
    df, error = load_data()
    
    if error:
        st.error(f"❌ {error}")
        st.info("Please ensure the merged CSV file exists at: `/mnt/user-data/outputs/research_opportunities_merged.csv`")
        return
    
    if df is None or len(df) == 0:
        st.warning("⚠️ No data available to display.")
        return
    
    # Sidebar filters
    filtered_df = apply_filters(df)
    
    # Main content
    create_metric_cards(filtered_df)
    
    st.markdown("---")
    
    # Tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Visualizations", "📋 Data Table", "🔍 Details", "ℹ️ About"])
    
    with tab1:
        if len(filtered_df) > 0:
            create_visualizations(filtered_df)
        else:
            st.warning("⚠️ No opportunities match the current filters. Try adjusting your criteria.")
    
    with tab2:
        if len(filtered_df) > 0:
            display_data_table(filtered_df)
        else:
            st.warning("⚠️ No opportunities match the current filters.")
    
    with tab3:
        if len(filtered_df) > 0:
            display_opportunity_details(filtered_df)
        else:
            st.warning("⚠️ No opportunities match the current filters.")
    
    with tab4:
        st.markdown("""
        ## About This Dashboard
        
        This interactive dashboard helps you explore research funding opportunities worldwide.
        
        ### Features:
        - 🔍 **Advanced Filtering**: Filter by location, duration, funding, field, and more
        - 📊 **Interactive Visualizations**: Explore data through dynamic charts
        - 📋 **Detailed Tables**: View and download filtered results
        - 🎯 **Opportunity Details**: Deep dive into individual programs
        
        ### Data Sources:
        This dashboard uses data compiled from:
        - European Programs (Batch 1)
        - Commonwealth & Oceanic Programs (Batch 2)
        - North American Programs (Batch 3)
        - Asian & Middle Eastern Programs (Batch 4)
        - Specialized Programs (Batch 5)
        
        ### How to Use:
        1. Use the **sidebar filters** to narrow down opportunities
        2. Explore **visualizations** to understand trends
        3. Check the **data table** for detailed listings
        4. View **individual details** for specific programs
        
        ### Need Help?
        - Adjust filters to see different results
        - Click "Reset All Filters" to start over
        - Download filtered data for offline analysis
        
        ---
        
        **Last Updated:** 2026-02-13
        """)

if __name__ == "__main__":
    main()
