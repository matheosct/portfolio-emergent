#!/usr/bin/env python3
"""
Backend API Testing Suite for Designer Portfolio
Tests the core API endpoints: /api/portfolio, /api/services, /api/projects
"""

import requests
import json
import sys
import os
from datetime import datetime

# Get the backend URL from frontend .env file
def get_backend_url():
    try:
        with open('/app/frontend/.env', 'r') as f:
            for line in f:
                if line.startswith('REACT_APP_BACKEND_URL='):
                    return line.split('=', 1)[1].strip()
    except FileNotFoundError:
        print("❌ Frontend .env file not found")
        return None
    return None

def test_portfolio_endpoint(base_url):
    """Test GET /api/portfolio endpoint"""
    print("\n🔍 Testing Portfolio Endpoint...")
    
    try:
        response = requests.get(f"{base_url}/api/portfolio", timeout=10)
        
        # Check status code
        if response.status_code != 200:
            print(f"❌ Portfolio endpoint failed with status {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
        # Check response format
        try:
            data = response.json()
        except json.JSONDecodeError:
            print("❌ Portfolio endpoint returned invalid JSON")
            return False
            
        # Verify response structure
        if not isinstance(data, dict) or not data.get('success'):
            print(f"❌ Portfolio endpoint missing success field or not dict: {data}")
            return False
            
        portfolio_data = data.get('data')
        if not portfolio_data:
            print("❌ Portfolio endpoint missing data field")
            return False
            
        # Check required fields
        required_fields = ['personal', 'about', 'navigation']
        missing_fields = []
        
        for field in required_fields:
            if field not in portfolio_data:
                missing_fields.append(field)
                
        if missing_fields:
            print(f"❌ Portfolio data missing fields: {missing_fields}")
            return False
            
        # Verify personal info structure
        personal = portfolio_data.get('personal', {})
        personal_required = ['name', 'title', 'email']
        personal_missing = [f for f in personal_required if not personal.get(f)]
        
        if personal_missing:
            print(f"❌ Personal info missing required fields: {personal_missing}")
            return False
            
        # Verify about info structure
        about = portfolio_data.get('about', {})
        if about and not isinstance(about, dict):
            print("❌ About section should be a dict")
            return False
            
        # Verify navigation structure
        navigation = portfolio_data.get('navigation', [])
        if not isinstance(navigation, list):
            print("❌ Navigation should be a list")
            return False
            
        # Check if ObjectID was converted to string id
        if 'id' not in portfolio_data:
            print("❌ Portfolio data missing 'id' field (ObjectID not converted)")
            return False
            
        print("✅ Portfolio endpoint working correctly")
        print(f"   - Personal: {personal.get('name')} ({personal.get('title')})")
        print(f"   - Email: {personal.get('email')}")
        print(f"   - Navigation items: {len(navigation)}")
        if about:
            print(f"   - Skills: {len(about.get('skills', []))}")
            print(f"   - Experience: {len(about.get('experience', []))}")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Portfolio endpoint request failed: {e}")
        return False

def test_services_endpoint(base_url):
    """Test GET /api/services endpoint"""
    print("\n🔍 Testing Services Endpoint...")
    
    try:
        response = requests.get(f"{base_url}/api/services", timeout=10)
        
        # Check status code
        if response.status_code != 200:
            print(f"❌ Services endpoint failed with status {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
        # Check response format
        try:
            data = response.json()
        except json.JSONDecodeError:
            print("❌ Services endpoint returned invalid JSON")
            return False
            
        # Verify response structure
        if not isinstance(data, dict) or not data.get('success'):
            print(f"❌ Services endpoint missing success field: {data}")
            return False
            
        services_data = data.get('data')
        if not isinstance(services_data, list):
            print(f"❌ Services data should be a list, got: {type(services_data)}")
            return False
            
        # Check if we have services
        if len(services_data) == 0:
            print("⚠️  No services found in database")
            return True  # This is not necessarily an error
            
        # Verify service structure
        for i, service in enumerate(services_data):
            if not isinstance(service, dict):
                print(f"❌ Service {i} is not a dict")
                return False
                
            # Check required fields
            required_fields = ['id', 'title', 'description']
            missing_fields = [f for f in required_fields if not service.get(f)]
            
            if missing_fields:
                print(f"❌ Service {i} missing fields: {missing_fields}")
                return False
                
            # Check optional fields exist
            if 'color' not in service:
                print(f"⚠️  Service {i} missing color field")
            if 'order' not in service:
                print(f"⚠️  Service {i} missing order field")
                
        # Check if services are ordered
        orders = [s.get('order', 0) for s in services_data]
        if orders != sorted(orders):
            print("⚠️  Services may not be properly ordered by 'order' field")
            
        print("✅ Services endpoint working correctly")
        print(f"   - Found {len(services_data)} services")
        for service in services_data[:3]:  # Show first 3
            print(f"   - {service.get('title')}: {service.get('description')[:50]}...")
            
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Services endpoint request failed: {e}")
        return False

def test_projects_endpoint(base_url):
    """Test GET /api/projects endpoint"""
    print("\n🔍 Testing Projects Endpoint...")
    
    try:
        response = requests.get(f"{base_url}/api/projects", timeout=10)
        
        # Check status code
        if response.status_code != 200:
            print(f"❌ Projects endpoint failed with status {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
        # Check response format
        try:
            data = response.json()
        except json.JSONDecodeError:
            print("❌ Projects endpoint returned invalid JSON")
            return False
            
        # Verify response structure
        if not isinstance(data, dict) or not data.get('success'):
            print(f"❌ Projects endpoint missing success field: {data}")
            return False
            
        projects_data = data.get('data')
        if not isinstance(projects_data, list):
            print(f"❌ Projects data should be a list, got: {type(projects_data)}")
            return False
            
        # Check if we have projects
        if len(projects_data) == 0:
            print("⚠️  No projects found in database")
            return True  # This is not necessarily an error
            
        # Verify project structure
        for i, project in enumerate(projects_data):
            if not isinstance(project, dict):
                print(f"❌ Project {i} is not a dict")
                return False
                
            # Check required fields
            required_fields = ['id', 'title', 'description']
            missing_fields = [f for f in required_fields if not project.get(f)]
            
            if missing_fields:
                print(f"❌ Project {i} missing fields: {missing_fields}")
                return False
                
            # Check optional fields exist
            optional_fields = ['category', 'bgColor', 'year', 'client', 'order']
            for field in optional_fields:
                if field not in project:
                    print(f"⚠️  Project {i} missing {field} field")
                    
            # Verify category is a list
            if 'category' in project and not isinstance(project['category'], list):
                print(f"❌ Project {i} category should be a list")
                return False
                
        # Check if projects are ordered
        orders = [p.get('order', 0) for p in projects_data]
        if orders != sorted(orders):
            print("⚠️  Projects may not be properly ordered by 'order' field")
            
        print("✅ Projects endpoint working correctly")
        print(f"   - Found {len(projects_data)} projects")
        for project in projects_data[:3]:  # Show first 3
            print(f"   - {project.get('title')}: {project.get('description')[:50]}...")
            if project.get('client'):
                print(f"     Client: {project.get('client')}, Year: {project.get('year', 'N/A')}")
            
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Projects endpoint request failed: {e}")
        return False

def main():
    """Main test runner"""
    print("🚀 Starting Designer Portfolio Backend API Tests")
    print("=" * 60)
    
    # Get backend URL
    backend_url = get_backend_url()
    if not backend_url:
        print("❌ Could not determine backend URL from frontend/.env")
        sys.exit(1)
        
    print(f"🌐 Testing backend at: {backend_url}")
    
    # Test basic connectivity
    try:
        response = requests.get(backend_url, timeout=5)
        print(f"✅ Backend is reachable (status: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"❌ Backend is not reachable: {e}")
        sys.exit(1)
    
    # Run tests
    test_results = []
    
    # Test portfolio endpoint
    test_results.append(("Portfolio", test_portfolio_endpoint(backend_url)))
    
    # Test services endpoint
    test_results.append(("Services", test_services_endpoint(backend_url)))
    
    # Test projects endpoint
    test_results.append(("Projects", test_projects_endpoint(backend_url)))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    for test_name, result in test_results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:20} {status}")
        if result:
            passed += 1
        else:
            failed += 1
    
    print(f"\nTotal: {passed + failed}, Passed: {passed}, Failed: {failed}")
    
    if failed > 0:
        print("\n❌ Some tests failed. Check the backend implementation.")
        sys.exit(1)
    else:
        print("\n🎉 All tests passed! Backend API is working correctly.")
        sys.exit(0)

if __name__ == "__main__":
    main()