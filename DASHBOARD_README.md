# Research Opportunities Dashboard

An interactive Streamlit dashboard for exploring global research funding opportunities with advanced filtering and visualization capabilities.

## 🚀 Features

### Advanced Filtering
- **🌍 Location**: Filter by country and region
- **⏱️ Duration**: Slide to select program length (in months)
- **💰 Funding Amount**: Filter by funding range (USD)
- **📚 Field of Study**: Select specific academic fields
- **👨‍🎓 Career Stage**: Filter by PhD, Master's, Post-doc, etc.
- **📋 Opportunity Type**: Fellowship, Scholarship, Grant, etc.
- **📅 Deadline**: Filter by upcoming, past, or no deadline

### Interactive Visualizations
- **Geographic Distribution**: Bar charts and pie charts showing opportunities by country/region
- **Funding Analysis**: Histograms of funding amounts
- **Career Stage Breakdown**: Distribution across career levels
- **Field Distribution**: Top fields of study
- **Timeline Analysis**: Deadline patterns by month and year
- **Competitiveness**: Acceptance rate categories

### Data Exploration
- **Detailed Table View**: Sortable, filterable table with all opportunities
- **Individual Details**: Deep dive into specific programs
- **CSV Export**: Download filtered results for offline analysis

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🔧 Installation

1. **Clone or download the project files**
   ```bash
   cd /path/to/your/project
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements_dashboard.txt
   ```

   Or install manually:
   ```bash
   pip install streamlit pandas plotly numpy openpyxl
   ```

3. **Ensure your merged CSV exists**
   Make sure you have run `merge_batches.py` first to create:
   ```
   /mnt/user-data/outputs/research_opportunities_merged.csv
   ```

## 🎮 Running the Dashboard

### Method 1: Command Line
```bash
streamlit run streamlit_dashboard.py
```

### Method 2: With Custom Port
```bash
streamlit run streamlit_dashboard.py --server.port 8501
```

### Method 3: From Python Script
```python
import os
os.system("streamlit run streamlit_dashboard.py")
```

## 🌐 Accessing the Dashboard

After running the command, Streamlit will:
1. Start a local server
2. Automatically open your default browser
3. Navigate to `http://localhost:8501`

If it doesn't open automatically, manually visit:
```
http://localhost:8501
```

## 📊 Using the Dashboard

### 1. **Sidebar Filters**
   - Located on the left side
   - Adjust any filter to update all visualizations
   - See active filter count at the bottom
   - Click "Reset All Filters" to clear selections

### 2. **Main Tabs**

   **📊 Visualizations Tab**
   - View interactive charts and graphs
   - Hover over charts for detailed information
   - Charts update automatically with filters

   **📋 Data Table Tab**
   - Browse all opportunities in table format
   - Scroll through results
   - Download filtered data as CSV

   **🔍 Details Tab**
   - Select individual programs from dropdown
   - View complete program information
   - Access application URLs

   **ℹ️ About Tab**
   - Dashboard information
   - Usage instructions
   - Data sources

### 3. **Key Metrics**
   - Top cards show summary statistics
   - Updates based on active filters
   - Quick overview of filtered results

## 🎯 Example Use Cases

### Find PhD Opportunities in Europe under $50k
1. Set **Region** to "Europe"
2. Set **Career Stage** to "Doctoral"
3. Adjust **Funding Amount** slider to max $50,000
4. View results in Visualizations or Table tabs

### Find STEM Fellowships with 2026 Deadlines
1. Set **Field of Study** to your STEM field
2. Set **Opportunity Type** to "Fellowship"
3. Set **Deadline** to "Upcoming (2026)"
4. Explore matching opportunities

### Compare Funding Across Regions
1. Leave all filters at "All"
2. View **Regional Distribution** pie chart
3. Click individual regions to filter
4. Compare funding distributions

## 🛠️ Troubleshooting

### Dashboard won't start
```bash
# Check Streamlit installation
streamlit --version

# Reinstall if needed
pip install --upgrade streamlit
```

### Data not loading
- Verify CSV path: `/mnt/user-data/outputs/research_opportunities_merged.csv`
- Run `merge_batches.py` if CSV is missing
- Check file permissions

### Port already in use
```bash
# Use a different port
streamlit run streamlit_dashboard.py --server.port 8502
```

### Filters not working
- Clear browser cache
- Refresh the page (F5)
- Click "Reset All Filters" button

## 📁 File Structure

```
project/
├── streamlit_dashboard.py          # Main dashboard application
├── requirements_dashboard.txt      # Python dependencies
├── merge_batches.py                # CSV merge script
├── explore_dataset.py              # Static analysis script
└── research_opportunities_merged.csv  # Data file (generated)
```

## 🔒 Data Privacy

- All data processing happens locally on your machine
- No data is sent to external servers
- CSV files remain on your local filesystem

## 📝 Customization

### Change Color Scheme
Edit the `st.markdown()` CSS section in `streamlit_dashboard.py`:
```python
.main-header {
    color: #your-color-here;
}
```

### Add New Filters
Add filter logic in the `apply_filters()` function:
```python
if 'your_column' in df.columns:
    selected_value = st.sidebar.selectbox("Label", options)
    filtered_df = filtered_df[filtered_df['your_column'] == selected_value]
```

### Modify Visualizations
Edit functions in `create_visualizations()`:
```python
fig = px.bar(data, x='x_col', y='y_col', title="Your Title")
st.plotly_chart(fig)
```

## 🆘 Support

For issues or questions:
1. Check the **About** tab in the dashboard
2. Review this README
3. Verify your Python/Streamlit versions
4. Ensure CSV data is properly formatted

## 📦 Export Options

### Export Filtered Data
1. Apply your desired filters
2. Go to **Data Table** tab
3. Click **📥 Download Filtered Data (CSV)**
4. File saves as `filtered_opportunities_YYYYMMDD.csv`

### Export Visualizations
- Right-click any chart
- Select "Save image as..."
- Choose PNG format

## 🔄 Updating Data

When you add new opportunities:
1. Update individual batch CSV files
2. Run `merge_batches.py` again
3. Restart the dashboard
4. New data will appear automatically

## 🌟 Tips for Best Experience

- **Use Chrome or Firefox** for best performance
- **Full screen mode** (F11) for better visualization
- **Wide layout** is enabled by default
- **Hover over charts** for interactive tooltips
- **Download data** before applying many filters
- **Reset filters** if results seem unexpected

## 📄 License

This dashboard is provided as-is for research and educational purposes.

## 🎓 Credits

Dashboard created for exploring global research funding opportunities compiled from:
- European programs
- Commonwealth & Oceanic programs
- North American programs
- Asian & Middle Eastern programs
- Specialized programs

---

**Version**: 1.0.0  
**Last Updated**: 2026-02-13  
**Dashboard Framework**: Streamlit  
**Visualization Library**: Plotly
