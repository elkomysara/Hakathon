"""
Script to merge all 5 batch CSV files into one complete dataset
Handles CSV parsing errors by reading with proper quoting
"""

import pandas as pd
import os

# Define the batch file names
batch_files = [
    'research_opportunities_batch1.csv',
    'research_opportunities_batch2.csv',
    'research_opportunities_batch3.csv',
    'research_opportunities_batch4.csv',
    'research_opportunities_batch5.csv'
]

# Directory containing the batch files
data_dir = '/mnt/user-data/outputs/'

# List to store dataframes
dfs = []

# Read each batch file with proper CSV handling
print("Reading batch files...")
for i, filename in enumerate(batch_files, 1):
    filepath = os.path.join(data_dir, filename)
    if os.path.exists(filepath):
        try:
            # Read with proper quoting and error handling
            df = pd.read_csv(
                filepath,
                encoding='utf-8',
                quotechar='"',
                escapechar='\\',
                on_bad_lines='warn',  # Warn about bad lines instead of failing
                engine='python'  # Use python engine for better error handling
            )
            print(f"✓ Batch {i}: {filename} - {len(df)} rows loaded")
            dfs.append(df)
        except Exception as e:
            print(f"✗ Error reading {filename}: {str(e)}")
            print(f"  Trying alternative parsing method...")
            try:
                # Try with different settings
                df = pd.read_csv(
                    filepath,
                    encoding='utf-8',
                    sep=',',
                    quotechar='"',
                    doublequote=True,
                    escapechar=None,
                    engine='python'
                )
                print(f"✓ Batch {i}: {filename} - {len(df)} rows loaded (alternative method)")
                dfs.append(df)
            except Exception as e2:
                print(f"✗ Failed to read {filename}: {str(e2)}")
    else:
        print(f"✗ Warning: {filename} not found at {filepath}")

# Concatenate all dataframes
if dfs:
    print("\n" + "="*60)
    print("Merging all batches...")
    print("="*60)
    
    # Check if all dataframes have the same columns
    all_columns = [set(df.columns) for df in dfs]
    if len(set(map(frozenset, all_columns))) > 1:
        print("Warning: Not all batches have the same columns!")
        for i, cols in enumerate(all_columns, 1):
            print(f"  Batch {i}: {len(cols)} columns")
    
    complete_df = pd.concat(dfs, ignore_index=True)
    
    # Sort by opportunity_id
    complete_df = complete_df.sort_values('opportunity_id').reset_index(drop=True)
    
    print(f"\n✓ Merged dataset: {len(complete_df)} total rows")
    print(f"✓ Columns: {len(complete_df.columns)}")
    print(f"✓ Opportunity IDs range: {complete_df['opportunity_id'].min()} to {complete_df['opportunity_id'].max()}")
    
    # Check for duplicates
    duplicates = complete_df['opportunity_id'].duplicated().sum()
    if duplicates > 0:
        print(f"\n✗ Warning: {duplicates} duplicate opportunity_id(s) found!")
        print("Duplicate IDs:")
        print(complete_df[complete_df['opportunity_id'].duplicated(keep=False)]['opportunity_id'].unique())
    else:
        print("\n✓ No duplicate opportunity_id found")
    
    # Check for missing critical fields
    critical_fields = [
        'opportunity_id', 'opportunity_name', 'institution_name', 
        'program_type', 'country', 'nationality_eligibility',
        'application_deadline', 'official_website', 'last_verified_date'
    ]
    
    print("\nChecking critical fields...")
    for field in critical_fields:
        if field in complete_df.columns:
            missing = complete_df[field].isna().sum()
            if missing > 0:
                print(f"  ✗ {field}: {missing} missing values")
            else:
                print(f"  ✓ {field}: complete")
        else:
            print(f"  ✗ {field}: column not found!")
    
    # Save merged file
    output_file = os.path.join(data_dir, 'research_opportunities_complete.csv')
    complete_df.to_csv(output_file, index=False, encoding='utf-8', quoting=1)  # quoting=1 means QUOTE_ALL
    print(f"\n✓ Merged file saved: {output_file}")
    
    # Display summary statistics
    print("\n" + "="*60)
    print("DATASET SUMMARY")
    print("="*60)
    print(f"Total opportunities: {len(complete_df)}")
    
    if 'program_type' in complete_df.columns:
        print(f"\nBy Program Type:")
        print(complete_df['program_type'].value_counts().to_string())
    
    if 'region' in complete_df.columns:
        print(f"\nBy Region:")
        print(complete_df['region'].value_counts().to_string())
    
    if 'academic_level' in complete_df.columns:
        print(f"\nBy Academic Level:")
        print(complete_df['academic_level'].value_counts().to_string())
    
    if 'field_of_study' in complete_df.columns:
        print(f"\nTop 10 Fields of Study:")
        print(complete_df['field_of_study'].value_counts().head(10).to_string())
    
    # Currency statistics
    if 'award_currency' in complete_df.columns:
        print(f"\nBy Currency:")
        print(complete_df['award_currency'].value_counts().to_string())
    
    print("\n" + "="*60)
    print("MERGE COMPLETE!")
    print("="*60)
    
else:
    print("\n✗ Error: No batch files found to merge!")
