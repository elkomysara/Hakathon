# 🚀 QUICK START GUIDE
## Research Opportunities Interactive Dashboard

### ⚡ Fastest Way to Get Started

**3 Simple Steps:**

```bash
# 1. Merge your data
python merge_batches.py

# 2. Install dependencies
pip install -r requirements_dashboard.txt

# 3. Launch dashboard
streamlit run streamlit_dashboard.py
```

**That's it!** Your dashboard will open at `http://localhost:8501` 🎉

---

## 📋 Prerequisites Checklist

- [ ] Python 3.8 or higher installed
- [ ] pip package manager available
- [ ] All 5 batch CSV files in the same directory:
  - `research_opportunities_batch1.csv`
  - `research_opportunities_batch2.csv`
  - `research_opportunities_batch3.csv`
  - `research_opportunities_batch4.csv`
  - `research_opportunities_batch5.csv`

### Check Your Python Version
```bash
python --version
# Should show Python 3.8.x or higher
```

---

## 🎯 Step-by-Step Installation

### **Step 1: Merge Data Files**

This combines all your batch CSVs into one master file.

```bash
python merge_batches.py
```

**Expected Output:**
```
✅ Successfully merged 5 batches
📊 Total opportunities: 75
💾 Saved to: research_opportunities_merged.csv
```

**Troubleshooting:**
- If you get "CSV not found" → Ensure batch files are in the same directory
- If you get "Parser error" → The enhanced script handles this automatically

---

### **Step 2: Install Required Packages**

#### Option A: Using Requirements File (Recommended)
```bash
pip install -r requirements_dashboard.txt
```

#### Option B: Manual Installation
```bash
pip install streamlit pandas plotly numpy openpyxl
```

**Expected Output:**
```
Successfully installed streamlit-1.31.0 pandas-2.2.0 plotly-5.18.0 ...
```

**Troubleshooting:**
- Permission error? Use: `pip install --user -r requirements_dashboard.txt`
- Slow download? Use: `pip install --no-cache-dir -r requirements_dashboard.txt`

---

### **Step 3: Launch the Dashboard**

#### Method 1: Direct Launch (Easiest)
```bash
streamlit run streamlit_dashboard.py
```

#### Method 2: Interactive Launcher
```bash
python launch_dashboard.py
```
This checks everything before launching!

#### Method 3: Shell Scripts

**Linux/Mac:**
```bash
chmod +x launch_dashboard.sh
./launch_dashboard.sh
```

**Windows:**
```cmd
launch_dashboard.bat
```

**Expected Output:**
```
🚀 Launching Dashboard...
  You can now view your Streamlit app in your browser.
  
  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

---

## 🎮 Using the Dashboard

### **Main Interface Overview**

```
┌─────────────────────────────────────────────────────────┐
│  🎓 Research Opportunities Explorer                     │
│  Discover and Filter Global Funding Opportunities       │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  [75 Opportunities] [50 Countries] [$45K Med] [5 Types] │
│                                                          │
├─────────────────────────────────────────────────────────┤
│  Tabs: [📊 Visualizations] [📋 Data Table] [🔍 Details] │
└─────────────────────────────────────────────────────────┘
```

### **Sidebar Filters (Left)**

1. **🌍 Location**
   - Country dropdown
   - Region selector

2. **⏱️ Duration**
   - Slider: 12-60 months
   - Drag to adjust range

3. **💰 Funding Amount**
   - Slider: $0-$200,000
   - Shows USD equivalent

4. **📚 Field of Study**
   - Dropdown: All fields
   - Select specific discipline

5. **👨‍🎓 Career Stage**
   - PhD, Master's, Post-doc
   - Early-career, etc.

6. **📋 Opportunity Type**
   - Fellowship
   - Scholarship
   - Research Grant
   - Training Program

7. **📅 Deadline**
   - All
   - Upcoming (2026)
   - Past deadlines
   - No deadline info

### **Active Filters Display**
```
🔍 3 active filters
📊 22 opportunities match
```

### **Reset Button**
Click **🔄 Reset All Filters** to clear selections

---

## 📊 Exploring the Data

### **Tab 1: Visualizations**

**What You'll See:**
- 🌍 **Geographic Distribution**: Bar chart + pie chart
- 💰 **Funding Analysis**: Histogram of amounts
- 🎓 **Career Stage**: Horizontal bar chart
- 📚 **Field Distribution**: Pie chart
- 📅 **Timeline**: Line chart by month
- 🎯 **Competitiveness**: Acceptance rates

**Pro Tips:**
- Hover over any chart for details
- Click pie slices to filter
- Charts update instantly with filters

### **Tab 2: Data Table**

**Features:**
- Sortable columns
- Scrollable list
- Direct links to applications
- Download filtered results

**Quick Actions:**
1. Click column headers to sort
2. Scroll to browse all entries
3. Click **📥 Download** for CSV export

### **Tab 3: Details**

**Individual Program View:**
1. Select program from dropdown
2. See complete information:
   - Institution details
   - Full eligibility criteria
   - Funding breakdown
   - Application deadlines
   - Direct application link

### **Tab 4: About**

- Dashboard documentation
- Data sources
- Usage instructions

---

## 💡 Example Workflows

### **Workflow 1: Find European PhD Opportunities**

1. **Set Filters:**
   - Region → "Europe"
   - Career Stage → "Doctoral"
   - Deadline → "Upcoming (2026)"

2. **Explore Results:**
   - Check Visualizations tab for distribution
   - Go to Data Table for full list
   - Click Details for specific programs

3. **Export:**
   - Click Download button
   - Save as CSV for applications

**Result:** ~12-15 matching opportunities

---

### **Workflow 2: Compare Funding Across Regions**

1. **Reset All Filters** (start fresh)

2. **View Visualizations:**
   - See "Regional Distribution" pie chart
   - Note percentages

3. **Filter by Region:**
   - Select "North America"
   - Check median funding
   - Repeat for other regions

**Result:** Compare funding ranges by geography

---

### **Workflow 3: Find STEM Fellowships Under $50K**

1. **Set Filters:**
   - Field → Select your STEM field
   - Type → "Fellowship"
   - Funding → Drag max to $50,000

2. **Review Table:**
   - Sort by deadline (click column)
   - Identify urgent applications

3. **Deep Dive:**
   - Switch to Details tab
   - Read full descriptions
   - Click application links

**Result:** Shortlist of target opportunities

---

## 🔧 Advanced Features

### **Multi-Filter Combinations**

Combine any filters for precise results:

```
Career Stage: PhD
+ Field: Computer Science
+ Country: United States
+ Funding: $40K-$60K
+ Deadline: Upcoming 2026
= ~5 highly targeted opportunities
```

### **Export Filtered Data**

1. Apply your filters
2. Go to **Data Table** tab
3. Click **📥 Download Filtered Data (CSV)**
4. File saves as: `filtered_opportunities_20260213.csv`

**Use Cases:**
- Import to Excel for tracking
- Share with colleagues
- Build application calendar

### **Save Visualizations**

**Method 1: Screenshot**
- Windows: `Win + Shift + S`
- Mac: `Cmd + Shift + 4`
- Linux: `PrtScn` or screenshot tool

**Method 2: Right-Click Chart**
- Click camera icon on chart
- Download as PNG

---

## 🛠️ Troubleshooting

### **Dashboard Won't Start**

**Error:** `streamlit: command not found`
```bash
# Solution: Reinstall Streamlit
pip install --upgrade streamlit

# Verify installation
streamlit --version
```

**Error:** `No module named 'streamlit'`
```bash
# Solution: Install in correct environment
python -m pip install streamlit
```

---

### **Data Not Loading**

**Error:** `Dataset not found`

**Solution:**
1. Check file exists:
   ```bash
   ls -la /mnt/user-data/outputs/research_opportunities_merged.csv
   ```
2. If missing, run merge script:
   ```bash
   python merge_batches.py
   ```

---

### **Port Already in Use**

**Error:** `Port 8501 is already in use`

**Solution 1:** Stop existing server
- Press `Ctrl+C` in terminal running Streamlit

**Solution 2:** Use different port
```bash
streamlit run streamlit_dashboard.py --server.port 8502
```

---

### **Charts Not Showing**

**Solution:**
1. Clear browser cache (Ctrl+Shift+Delete)
2. Refresh page (F5)
3. Try different browser (Chrome recommended)

---

### **Filters Not Working**

**Solution:**
1. Click **Reset All Filters**
2. Apply filters one at a time
3. Check console for errors (F12)

---

## 📱 Accessing from Other Devices

### **Same Network Access**

When dashboard starts, note the **Network URL**:
```
Local URL: http://localhost:8501
Network URL: http://192.168.1.100:8501  ← Use this
```

**On Other Device:**
1. Connect to same WiFi
2. Open browser
3. Navigate to Network URL
4. Dashboard loads remotely!

**Use Cases:**
- Present to team on projector
- Access from tablet
- Share with colleague

---

## 🎯 Tips for Best Experience

### **Performance**
- ✅ Use Chrome or Firefox
- ✅ Close unnecessary tabs
- ✅ Disable ad blockers for localhost

### **Workflow**
- ✅ Start with broad filters, narrow down
- ✅ Export data before applying many filters
- ✅ Use Details tab for final decisions

### **Data Management**
- ✅ Download filtered results regularly
- ✅ Keep batch CSVs as backup
- ✅ Re-merge after updating data

---

## 📚 Learning Resources

### **Streamlit Basics**
- [Official Tutorial](https://docs.streamlit.io/library/get-started)
- [Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)

### **Plotly Charts**
- [Gallery](https://plotly.com/python/)
- [Examples](https://plotly.com/python/basic-charts/)

### **Pandas Data**
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

---

## 🆘 Getting Help

### **In-Dashboard Help**
1. Click **About** tab
2. Read usage instructions
3. Check troubleshooting section

### **Command Line Help**
```bash
streamlit --help
streamlit run --help
```

### **Check Versions**
```bash
streamlit --version
python --version
pip list | grep streamlit
```

---

## 🎉 You're Ready!

### **Final Checklist:**
- [x] Merged data file created
- [x] Dependencies installed
- [x] Dashboard launched successfully
- [x] Filters working
- [x] Visualizations loading

### **Next Steps:**
1. **Explore** the full dataset
2. **Filter** to your interests
3. **Export** your shortlist
4. **Apply** to opportunities!

---

## 📧 Share This Guide

This guide covers everything from installation to advanced usage. Share with colleagues or students who need to:
- Explore research opportunities
- Filter funding options
- Analyze academic programs
- Track application deadlines

---

**Version:** 1.0.0  
**Last Updated:** 2026-02-13  
**Questions?** Check `DASHBOARD_README.md` for detailed documentation

**Good luck with your research journey! 🎓🚀**
