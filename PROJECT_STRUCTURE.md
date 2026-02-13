# Research Opportunities Project Structure

## 📁 Complete File List

```
research-opportunities-dashboard/
│
├── 📊 DATA FILES
│   ├── research_opportunities_batch1.csv      # European Programs (15 entries)
│   ├── research_opportunities_batch2.csv      # Commonwealth & Oceanic (15 entries)
│   ├── research_opportunities_batch3.csv      # North American (15 entries)
│   ├── research_opportunities_batch4.csv      # Asian & Middle Eastern (15 entries)
│   ├── research_opportunities_batch5.csv      # Specialized Programs (15 entries)
│   └── research_opportunities_merged.csv      # Complete dataset (75 entries)
│
├── 🐍 PYTHON SCRIPTS
│   ├── merge_batches.py                       # Merge all CSV batches into one
│   ├── explore_dataset.py                     # Static analysis & visualizations
│   ├── streamlit_dashboard.py                 # Interactive Streamlit dashboard
│   └── launch_dashboard.py                    # Quick start Python launcher
│
├── 💻 LAUNCH SCRIPTS
│   ├── launch_dashboard.sh                    # Linux/Mac launcher
│   └── launch_dashboard.bat                   # Windows launcher
│
├── 📋 CONFIGURATION
│   └── requirements_dashboard.txt             # Python dependencies
│
├── 📚 DOCUMENTATION
│   ├── DASHBOARD_README.md                    # Dashboard user guide
│   └── PROJECT_STRUCTURE.md                   # This file
│
└── 📈 OUTPUTS (Generated)
    ├── country_distribution.png               # Geographic bar chart
    ├── region_distribution.png                # Regional pie chart
    ├── opportunity_types.png                  # Types bar chart
    ├── deadline_months_*.png                  # Timeline analysis
    ├── career_stages.png                      # Career distribution
    ├── program_features.png                   # Features analysis
    ├── competitiveness.png                    # Acceptance rates
    └── dataset_summary_report.txt             # Text summary report
```

## 🔧 Setup Workflow

### Step 1: Merge Data
```bash
python merge_batches.py
```
**Output**: `research_opportunities_merged.csv`

### Step 2: Explore Data (Optional)
```bash
python explore_dataset.py
```
**Output**: Multiple PNG charts + summary report

### Step 3: Launch Dashboard
```bash
# Option A: Python launcher
python launch_dashboard.py

# Option B: Direct Streamlit
streamlit run streamlit_dashboard.py

# Option C: Shell script (Linux/Mac)
chmod +x launch_dashboard.sh
./launch_dashboard.sh

# Option D: Batch file (Windows)
launch_dashboard.bat
```

## 📊 Dashboard Features

### Filters (Sidebar)
- 🌍 **Location**: Country & Region
- ⏱️ **Duration**: Slider (months)
- 💰 **Funding**: Amount range (USD)
- 📚 **Field**: Academic disciplines
- 👨‍🎓 **Career Stage**: PhD, Master's, etc.
- 📋 **Type**: Fellowship, Scholarship, Grant
- 📅 **Deadline**: Upcoming/Past/None

### Visualizations
- Geographic distribution (bar + pie)
- Funding histograms
- Career stage breakdown
- Field of study analysis
- Timeline by month
- Competitiveness categories

### Data Views
- **Table**: Sortable, downloadable CSV
- **Details**: Individual program explorer
- **About**: Documentation

## 🎯 Key Files Explained

### `merge_batches.py`
- Combines all 5 batch CSVs
- Validates column consistency
- Checks for duplicates
- Generates summary statistics
- Exports merged CSV

### `explore_dataset.py`
- Loads merged CSV
- Generates static visualizations
- Creates summary report
- Exports PNG charts
- No interactivity (one-time analysis)

### `streamlit_dashboard.py`
- Interactive web application
- Real-time filtering
- Dynamic visualizations (Plotly)
- Data export
- Program details view

### `launch_dashboard.py`
- Checks Python installation
- Verifies dependencies
- Validates data file
- Launches Streamlit server
- User-friendly prompts

## 📦 Dependencies

### Core Libraries
- **streamlit**: Web dashboard framework
- **pandas**: Data manipulation
- **plotly**: Interactive charts
- **numpy**: Numerical operations
- **matplotlib**: Static plots (explore_dataset.py)
- **seaborn**: Enhanced styling (explore_dataset.py)

### Installation
```bash
pip install -r requirements_dashboard.txt
```

Or individually:
```bash
pip install streamlit pandas plotly numpy matplotlib seaborn
```

## 🌐 Running on Different Systems

### Linux / macOS
```bash
# Make script executable
chmod +x launch_dashboard.sh

# Run
./launch_dashboard.sh
```

### Windows
```cmd
# Double-click launch_dashboard.bat
# Or from Command Prompt:
launch_dashboard.bat
```

### Any Platform (Python)
```bash
python launch_dashboard.py
```

## 📁 Data File Locations

### Input Files
- Batch CSVs should be in the same directory as scripts
- Or specify custom path in `merge_batches.py`:
  ```python
  batch_files = [
      'path/to/research_opportunities_batch1.csv',
      # ...
  ]
  ```

### Output Files
- Merged CSV: `/mnt/user-data/outputs/research_opportunities_merged.csv`
- Charts: `/mnt/user-data/outputs/*.png`
- Report: `/mnt/user-data/outputs/dataset_summary_report.txt`

### Dashboard Exports
- Filtered CSVs: `filtered_opportunities_YYYYMMDD.csv`
- Downloaded to user's default download folder

## 🔄 Updating Data

### Add New Opportunities
1. Update individual batch CSV files
2. Re-run `merge_batches.py`
3. Restart dashboard (Ctrl+C → relaunch)
4. Changes appear immediately

### Add New Batches
1. Create `research_opportunities_batch6.csv`
2. Edit `merge_batches.py`:
   ```python
   batch_files = [
       'research_opportunities_batch1.csv',
       # ...
       'research_opportunities_batch6.csv',  # Add new
   ]
   ```
3. Run merge script
4. Dashboard auto-loads new data

## 🎨 Customization

### Change Dashboard Colors
Edit `streamlit_dashboard.py`:
```python
st.markdown("""
    <style>
    .main-header {
        color: #YOUR_COLOR;  # Change header color
    }
    </style>
""", unsafe_allow_html=True)
```

### Add New Filters
In `apply_filters()` function:
```python
if 'your_new_column' in df.columns:
    selected = st.sidebar.selectbox("Label", options)
    filtered_df = filtered_df[filtered_df['your_new_column'] == selected]
```

### Modify Charts
In `create_visualizations()`:
```python
fig = px.bar(data, x='col1', y='col2', 
             title="Your Title",
             color_discrete_sequence=['#YOUR_COLOR'])
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Use different port
streamlit run streamlit_dashboard.py --server.port 8502
```

### CSV Not Found
```bash
# Check path
ls -la /mnt/user-data/outputs/research_opportunities_merged.csv

# Re-run merge
python merge_batches.py
```

### Package Errors
```bash
# Reinstall all
pip install --upgrade -r requirements_dashboard.txt

# Or individually
pip install --upgrade streamlit pandas plotly
```

### Dashboard Won't Start
```bash
# Check Streamlit version
streamlit --version

# Should be >= 1.30.0
pip install --upgrade streamlit
```

## 📊 Performance Tips

### Large Datasets
- Dashboard tested with 75 entries
- Should handle 1,000+ entries smoothly
- For 10,000+ entries, consider:
  - Pagination in table view
  - Caching optimizations
  - Chunked loading

### Optimization
```python
# Already implemented in dashboard:
@st.cache_data  # Caches data loading
def load_data():
    # ...
```

## 🔒 Security

### Local Only
- Dashboard runs on `localhost:8501`
- No external connections
- Data stays on your machine

### Deploy Publicly (Advanced)
- Use Streamlit Cloud (free)
- Or deploy to Heroku/AWS/Azure
- Ensure data privacy compliance

## 📝 Version History

- **v1.0.0** (2026-02-13)
  - Initial release
  - 5 batches, 75 opportunities
  - Complete filtering system
  - Interactive visualizations
  - Export capabilities

## 🆘 Support Resources

### Documentation
- [Streamlit Docs](https://docs.streamlit.io)
- [Plotly Documentation](https://plotly.com/python/)
- [Pandas Guide](https://pandas.pydata.org/docs/)

### Quick Links
- Dashboard README: `DASHBOARD_README.md`
- This guide: `PROJECT_STRUCTURE.md`
- Requirements: `requirements_dashboard.txt`

---

**Project Structure Version**: 1.0.0  
**Last Updated**: 2026-02-13
