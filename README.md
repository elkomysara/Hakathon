# 🎓 Research Opportunities Interactive Dashboard

**Complete Package for Exploring Global Research Funding Opportunities**

---

## 📦 What You've Got

A **fully functional Streamlit dashboard** with advanced filtering, interactive visualizations, and data export capabilities for exploring 75 research opportunities across 50+ countries.

### 📁 **11 Files Created** (Total: ~93 KB)

| File | Size | Purpose |
|------|------|---------|
| `streamlit_dashboard.py` | 23 KB | **Main dashboard application** |
| `explore_dataset.py` | 15 KB | Static analysis & PNG charts |
| `QUICKSTART.md` | 11 KB | **Start here!** Installation guide |
| `PROJECT_STRUCTURE.md` | 8.2 KB | Technical architecture |
| `DASHBOARD_README.md` | 7.0 KB | Complete user manual |
| `merge_batches.py` | 5.3 KB | Data processing script |
| `launch_dashboard.py` | 3.7 KB | Interactive launcher |
| `FILES_SUMMARY.txt` | 17 KB | Visual package overview |
| `launch_dashboard.sh` | 1.5 KB | Linux/Mac launcher |
| `launch_dashboard.bat` | 1.5 KB | Windows launcher |
| `requirements_dashboard.txt` | 77 B | Python dependencies |

---

## 🚀 Quick Start (3 Commands)

```bash
# 1. Merge your CSV batches
python merge_batches.py

# 2. Install dependencies
pip install -r requirements_dashboard.txt

# 3. Launch dashboard
streamlit run streamlit_dashboard.py
```

**Dashboard opens at:** `http://localhost:8501` 🎉

---

## ⭐ Key Features

### 🔍 **Advanced Filtering System**
Filter by 7 criteria simultaneously:
- 🌍 **Location**: Country & Region
- ⏱️ **Duration**: Slider (months)
- 💰 **Funding**: Amount range (USD)
- 📚 **Field**: Academic disciplines
- 👨‍🎓 **Career Stage**: PhD, Master's, Post-doc, etc.
- 📋 **Type**: Fellowship, Scholarship, Grant
- 📅 **Deadline**: Upcoming/Past/None

### 📊 **Interactive Visualizations**
- Geographic distribution (bar charts + pie charts)
- Funding amount histograms
- Career stage breakdown
- Field of study analysis
- Timeline analysis (monthly deadlines)
- Competitiveness categories (acceptance rates)

### 📋 **Data Management**
- Sortable, filterable data tables
- CSV export of filtered results
- Individual program detail views
- Direct application URL links

---

## 📖 Documentation Guide

**Where to Start?**

1. **New to the project?**  
   → Read [`QUICKSTART.md`](computer:///mnt/user-data/outputs/QUICKSTART.md) (3-minute read)

2. **Want comprehensive guide?**  
   → Check [`DASHBOARD_README.md`](computer:///mnt/user-data/outputs/DASHBOARD_README.md)

3. **Need technical details?**  
   → Review [`PROJECT_STRUCTURE.md`](computer:///mnt/user-data/outputs/PROJECT_STRUCTURE.md)

4. **Want visual overview?**  
   → See [`FILES_SUMMARY.txt`](computer:///mnt/user-data/outputs/FILES_SUMMARY.txt)

---

## 🎯 Usage Examples

### **Example 1: Find European PhD Programs**
```
Filters:
  Region = Europe
  Career Stage = Doctoral
  Deadline = Upcoming (2026)

Result: ~12-15 opportunities
```

### **Example 2: STEM Fellowships Under $50K**
```
Filters:
  Field = STEM
  Type = Fellowship
  Funding ≤ $50,000

Result: ~8-10 targeted opportunities
```

### **Example 3: Compare Regional Funding**
```
Steps:
  1. View Regional Distribution pie chart
  2. Filter by each region
  3. Note median funding amounts

Result: Comparative analysis across regions
```

---

## 💻 Platform Support

### **Windows**
```cmd
# Double-click to launch:
launch_dashboard.bat

# Or use Python:
python launch_dashboard.py
```

### **Linux / macOS**
```bash
# Make executable:
chmod +x launch_dashboard.sh

# Run:
./launch_dashboard.sh

# Or use Python:
python launch_dashboard.py
```

### **Any Platform**
```bash
# Direct Streamlit:
streamlit run streamlit_dashboard.py

# Interactive launcher:
python launch_dashboard.py
```

---

## 📊 Dataset Overview

**75 Research Opportunities** across **5 Batches:**

| Batch | Region | Count | IDs |
|-------|--------|-------|-----|
| 1 | European Programs | 15 | OP0001-OP0015 |
| 2 | Commonwealth & Oceanic | 15 | OP0016-OP0030 |
| 3 | North American | 15 | OP0031-OP0045 |
| 4 | Asian & Middle Eastern | 15 | OP0046-OP0060 |
| 5 | Specialized Programs | 15 | OP0061-OP0075 |

**Coverage:**
- 50+ Countries
- 5 Continents
- $15K-$200K Funding Range
- PhD, Master's, Post-doc, Early-career
- All academic fields

---

## 🛠️ Requirements

### **System**
- Python 3.8 or higher
- 2 GB RAM minimum (4 GB recommended)
- 100 MB free disk space
- Modern web browser (Chrome, Firefox, Safari, Edge)

### **Python Packages**
```txt
streamlit==1.31.0
pandas==2.2.0
plotly==5.18.0
numpy==1.26.3
openpyxl==3.1.2
```

**Install with:**
```bash
pip install -r requirements_dashboard.txt
```

---

## 🎨 Dashboard Features

### **Sidebar Filters (Left)**
- Real-time filter application
- Active filter counter
- One-click reset button
- Match count display

### **Main Tabs**
1. **📊 Visualizations**: Interactive charts (Plotly)
2. **📋 Data Table**: Sortable list with export
3. **🔍 Details**: Individual program explorer
4. **ℹ️ About**: Documentation & help

### **Top Metrics Cards**
- Total opportunities count
- Number of countries
- Median funding amount
- Opportunity types

---

## 🔧 Troubleshooting

### **Dashboard won't start?**
```bash
# Check Python version
python --version  # Should be 3.8+

# Check Streamlit
streamlit --version

# Reinstall if needed
pip install --upgrade streamlit
```

### **Data not loading?**
```bash
# Ensure merged CSV exists
ls -la /mnt/user-data/outputs/research_opportunities_merged.csv

# If missing, run merge:
python merge_batches.py
```

### **Port already in use?**
```bash
# Use different port
streamlit run streamlit_dashboard.py --server.port 8502
```

### **Filters not working?**
- Click "Reset All Filters" button
- Refresh browser (F5)
- Clear browser cache (Ctrl+Shift+Delete)

---

## 📥 Export Options

### **Filtered Data**
1. Apply your filters
2. Go to **Data Table** tab
3. Click **📥 Download Filtered Data (CSV)**
4. File saves as: `filtered_opportunities_YYYYMMDD.csv`

### **Visualizations**
- Right-click any chart
- Click camera icon
- Download as PNG

---

## 🔄 Updating Data

**When you add new opportunities:**

1. Update individual batch CSV files
2. Run merge script:
   ```bash
   python merge_batches.py
   ```
3. Restart dashboard (Ctrl+C → relaunch)
4. New data appears automatically!

---

## 🎓 Example Workflows

### **Workflow 1: Application Planning**
```
Goal: Build application timeline
Steps:
  1. Filter by deadline = "Upcoming (2026)"
  2. Sort by deadline (earliest first)
  3. Export filtered data
  4. Create application calendar in Excel

Result: Organized application schedule
```

### **Workflow 2: Funding Comparison**
```
Goal: Find best-funded opportunities
Steps:
  1. Set career stage filter
  2. View funding histogram
  3. Filter by top funding range
  4. Compare programs in Details tab

Result: Shortlist of highest-paying programs
```

### **Workflow 3: Geographic Search**
```
Goal: Explore opportunities in target country
Steps:
  1. Select country from dropdown
  2. Review all matching opportunities
  3. Check eligibility in Details tab
  4. Save application URLs

Result: Country-specific opportunity list
```

---

## 🌟 Pro Tips

### **Performance**
- ✅ Use Chrome or Firefox for best experience
- ✅ Close unnecessary browser tabs
- ✅ Dashboard caches data automatically

### **Workflow**
- ✅ Start broad, then narrow filters
- ✅ Export data before heavy filtering
- ✅ Use Details tab for final decisions
- ✅ Reset filters when changing search strategy

### **Data Analysis**
- ✅ Hover over charts for detailed tooltips
- ✅ Compare regions using pie charts
- ✅ Track deadlines with timeline view
- ✅ Sort table by any column

---

## 📚 Additional Scripts

### **Static Analysis**
Generate PNG charts and summary reports:
```bash
python explore_dataset.py
```

**Outputs:**
- `country_distribution.png`
- `region_distribution.png`
- `opportunity_types.png`
- `career_stages.png`
- `program_features.png`
- `competitiveness.png`
- `dataset_summary_report.txt`

---

## 🔒 Privacy & Security

- ✅ **100% local**: All processing on your machine
- ✅ **No external calls**: Data stays private
- ✅ **No tracking**: Zero analytics or telemetry
- ✅ **Open source**: Review all code

---

## 🆘 Support Resources

### **Documentation Files**
- [`QUICKSTART.md`](computer:///mnt/user-data/outputs/QUICKSTART.md) - Quick installation guide
- [`DASHBOARD_README.md`](computer:///mnt/user-data/outputs/DASHBOARD_README.md) - Complete manual
- [`PROJECT_STRUCTURE.md`](computer:///mnt/user-data/outputs/PROJECT_STRUCTURE.md) - Technical details
- [`FILES_SUMMARY.txt`](computer:///mnt/user-data/outputs/FILES_SUMMARY.txt) - Visual overview

### **Online Resources**
- [Streamlit Documentation](https://docs.streamlit.io)
- [Plotly Charts Gallery](https://plotly.com/python/)
- [Pandas User Guide](https://pandas.pydata.org/docs/)

---

## 🎯 Next Steps

### **Immediate Actions:**
1. ✅ Read [`QUICKSTART.md`](computer:///mnt/user-data/outputs/QUICKSTART.md) (5 minutes)
2. ✅ Run `python merge_batches.py`
3. ✅ Install dependencies: `pip install -r requirements_dashboard.txt`
4. ✅ Launch dashboard: `streamlit run streamlit_dashboard.py`
5. ✅ Explore your data!

### **Advanced Usage:**
- Customize filters (edit `streamlit_dashboard.py`)
- Add new visualizations (modify `create_visualizations()`)
- Change color schemes (update CSS in dashboard)
- Deploy to Streamlit Cloud (for public access)

---

## 📊 Statistics

**Package Contents:**
- 11 files created
- ~93 KB total size
- 3 launcher scripts (Python, Bash, Batch)
- 4 comprehensive documentation files
- 2 data processing scripts
- 1 interactive dashboard
- 1 dependency file

**Dashboard Capabilities:**
- 7 filter types
- 6 visualization categories
- 4 view tabs
- 75 opportunities
- 50+ countries
- 100% interactive

---

## 🎉 You're All Set!

Everything you need is in `/mnt/user-data/outputs/`:

```
✅ Dashboard application (streamlit_dashboard.py)
✅ Launcher scripts (launch_dashboard.*)
✅ Dependencies (requirements_dashboard.txt)
✅ Documentation (*.md files)
✅ Data processing (merge_batches.py, explore_dataset.py)
```

**Ready to launch?**
```bash
python launch_dashboard.py
```

**Good luck with your research journey! 🎓🚀**

---

## 📝 Version Information

- **Package Version**: 1.0.0
- **Release Date**: 2026-02-13
- **Dashboard Framework**: Streamlit 1.31.0
- **Visualization Library**: Plotly 5.18.0
- **Data Processing**: Pandas 2.2.0

---

## 📧 File Locations

All files are saved in:
```
/mnt/user-data/outputs/
```

**Quick Access Links:**
- [streamlit_dashboard.py](computer:///mnt/user-data/outputs/streamlit_dashboard.py)
- [launch_dashboard.py](computer:///mnt/user-data/outputs/launch_dashboard.py)
- [requirements_dashboard.txt](computer:///mnt/user-data/outputs/requirements_dashboard.txt)
- [QUICKSTART.md](computer:///mnt/user-data/outputs/QUICKSTART.md)
- [FILES_SUMMARY.txt](computer:///mnt/user-data/outputs/FILES_SUMMARY.txt)

---

**© 2026 Research Opportunities Explorer**  
*Making research funding accessible to everyone* 🌍
