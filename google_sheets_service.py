import json
import os
from typing import Dict, List, Any
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class GoogleSheetsService:
    def __init__(self):
        self.service = None
        self.spreadsheet_id = None
        self.worksheet_name = "Consultations"
        self._initialize_service()
    
    def _initialize_service(self):
        """Initialize Google Sheets service with service account credentials."""
        try:
            # For demo purposes, we'll create a mock service
            # In production, you would use actual service account credentials
            print("Google Sheets service initialized (mock mode)")
            self.service = "mock_service"
            self.spreadsheet_id = "demo_spreadsheet_id"
        except Exception as e:
            print(f"Error initializing Google Sheets service: {e}")
            self.service = None
    
    def create_spreadsheet(self, title: str) -> str:
        """Create a new spreadsheet and return its ID."""
        try:
            if not self.service:
                return "mock_spreadsheet_id"
            
            # Mock implementation
            print(f"Created spreadsheet: {title}")
            return "mock_spreadsheet_id"
            
        except Exception as e:
            print(f"Error creating spreadsheet: {e}")
            return None
    
    def setup_consultation_headers(self, spreadsheet_id: str = None):
        """Set up the headers for the consultation data."""
        if not spreadsheet_id:
            spreadsheet_id = self.spreadsheet_id
        
        headers = [
            "ID",
            "Name", 
            "Phone",
            "Email",
            "Age",
            "Gender",
            "Medical Conditions",
            "Consultation Type",
            "Date",
            "Time",
            "Created At",
            "Status"
        ]
        
        try:
            # Mock implementation
            print(f"Headers set up for spreadsheet {spreadsheet_id}: {headers}")
            return True
        except Exception as e:
            print(f"Error setting up headers: {e}")
            return False
    
    def append_consultation_data(self, consultation_data: Dict[str, Any], spreadsheet_id: str = None) -> bool:
        """Append consultation data to the spreadsheet."""
        if not spreadsheet_id:
            spreadsheet_id = self.spreadsheet_id
        
        try:
            # Convert consultation data to row format
            row_data = [
                consultation_data.get('id', ''),
                consultation_data.get('name', ''),
                consultation_data.get('phone', ''),
                consultation_data.get('email', ''),
                str(consultation_data.get('age', '')),
                consultation_data.get('gender', ''),
                ', '.join(consultation_data.get('medicalConditions', [])),
                consultation_data.get('consultationType', ''),
                consultation_data.get('date', ''),
                consultation_data.get('time', ''),
                consultation_data.get('createdAt', ''),
                consultation_data.get('status', 'pending')
            ]
            
            # Mock implementation - in production this would append to actual Google Sheets
            print(f"Appending data to spreadsheet {spreadsheet_id}:")
            print(f"Row data: {row_data}")
            
            # Simulate successful append
            return True
            
        except Exception as e:
            print(f"Error appending consultation data: {e}")
            return False
    
    def get_consultation_data(self, spreadsheet_id: str = None) -> List[Dict[str, Any]]:
        """Retrieve all consultation data from the spreadsheet."""
        if not spreadsheet_id:
            spreadsheet_id = self.spreadsheet_id
        
        try:
            # Mock implementation - return sample data
            sample_data = [
                {
                    'id': '1',
                    'name': 'John Doe',
                    'phone': '+91 9876543210',
                    'email': 'john@example.com',
                    'age': 35,
                    'gender': 'Male',
                    'medicalConditions': ['Diabetes', 'Thyroid'],
                    'consultationType': 'Online',
                    'date': '2024-01-15',
                    'time': '10:00 AM',
                    'createdAt': '2024-01-10T09:00:00Z',
                    'status': 'pending'
                }
            ]
            
            print(f"Retrieved {len(sample_data)} consultation records")
            return sample_data
            
        except Exception as e:
            print(f"Error retrieving consultation data: {e}")
            return []
    
    def update_consultation_status(self, consultation_id: str, status: str, spreadsheet_id: str = None) -> bool:
        """Update the status of a specific consultation."""
        if not spreadsheet_id:
            spreadsheet_id = self.spreadsheet_id
        
        try:
            # Mock implementation
            print(f"Updated consultation {consultation_id} status to {status}")
            return True
            
        except Exception as e:
            print(f"Error updating consultation status: {e}")
            return False

# Global instance
google_sheets_service = GoogleSheetsService()

