import requests
import os

def test_upload():
    url = "http://127.0.0.1:5000/api/upload"
    
    # Create sample CSV with exact column names
    sample_csv = """transaction_id,amount,customer_id,merchant,date,category,location
TX001,150.50,CUST001,Amazon,2024-01-15,Electronics,Online
TX002,25.75,CUST002,Starbucks,2024-01-15,Food,Seattle
TX003,1200.00,CUST003,Best Buy,2024-01-16,Electronics,New York
TX004,45.00,CUST004,McDonald's,2024-01-16,Food,Chicago
TX005,2000.00,CUST007,foodmandu,2024-01-19,Food,Kathmandu
"""
    
    # Save to file
    with open('sample_data.csv', 'w') as f:
        f.write(sample_csv)
    
    print("📤 Testing file upload...")
    
    try:
        with open('sample_data.csv', 'rb') as file:
            files = {'file': ('sample_data.csv', file, 'text/csv')}
            response = requests.post(url, files=files)
        
        print(f"📊 Response Status: {response.status_code}")
        print(f"📊 Response Text: {response.text}")
        
        if response.status_code == 200:
            print("🎉 Upload successful!")
        else:
            print("❌ Upload failed")
            
    except Exception as e:
        print(f"💥 Error: {e}")

if __name__ == "__main__":
    test_upload()