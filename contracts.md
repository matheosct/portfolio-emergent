# API Contracts - Designer Portfolio Backend

## Overview
This document defines the API contracts for converting the designer portfolio from mock data to a fully functional backend system with MongoDB.

## Current Mock Data Structure (mock.js)

### 1. Personal Information
```javascript
personal: {
  name, title, tagline, email, phone, location
}
```

### 2. Services
```javascript
services: [
  { id, title, description, color }
]
```

### 3. Projects
```javascript
projects: [
  { id, title, description, category[], bgColor, year, client }
]
```

### 4. About Information
```javascript
about: {
  bio, 
  experience: [{ role, company, period }],
  skills: [string]
}
```

### 5. Navigation
```javascript
navigation: [
  { name, href }
]
```

## Backend Implementation Plan

### Database Models

#### 1. Portfolio Model (`portfolios` collection)
```javascript
{
  _id: ObjectId,
  personal: {
    name: String (required),
    title: String (required),
    tagline: String,
    email: String (required),
    phone: String,
    location: String
  },
  about: {
    bio: String,
    experience: [{
      role: String,
      company: String,
      period: String
    }],
    skills: [String]
  },
  navigation: [{
    name: String,
    href: String
  }],
  created_at: DateTime,
  updated_at: DateTime
}
```

#### 2. Service Model (`services` collection)
```javascript
{
  _id: ObjectId,
  title: String (required),
  description: String (required),
  color: String,
  order: Number,
  active: Boolean (default: true),
  created_at: DateTime,
  updated_at: DateTime
}
```

#### 3. Project Model (`projects` collection)
```javascript
{
  _id: ObjectId,
  title: String (required),
  description: String (required),
  category: [String],
  bgColor: String,
  year: String,
  client: String,
  order: Number,
  active: Boolean (default: true),
  created_at: DateTime,
  updated_at: DateTime
}
```

## API Endpoints

### Portfolio Endpoints
- `GET /api/portfolio` - Get portfolio information (personal + about + navigation)
- `PUT /api/portfolio` - Update portfolio information

### Services Endpoints
- `GET /api/services` - Get all active services (ordered)
- `POST /api/services` - Create new service
- `PUT /api/services/{id}` - Update service
- `DELETE /api/services/{id}` - Delete service

### Projects Endpoints
- `GET /api/projects` - Get all active projects (ordered)
- `POST /api/projects` - Create new project
- `PUT /api/projects/{id}` - Update project
- `DELETE /api/projects/{id}` - Delete project

## API Response Formats

### GET /api/portfolio
```javascript
{
  "success": true,
  "data": {
    "personal": { ... },
    "about": { ... },
    "navigation": [ ... ]
  }
}
```

### GET /api/services
```javascript
{
  "success": true,
  "data": [
    {
      "id": "string",
      "title": "string",
      "description": "string",
      "color": "string"
    }
  ]
}
```

### GET /api/projects
```javascript
{
  "success": true,
  "data": [
    {
      "id": "string",
      "title": "string",
      "description": "string",
      "category": ["string"],
      "bgColor": "string",
      "year": "string",
      "client": "string"
    }
  ]
}
```

## Frontend Integration Plan

### 1. Create API Service Layer
- Create `src/services/api.js` for centralized API calls
- Use axios for HTTP requests
- Handle loading states and errors

### 2. Update Components
- **App.js**: Replace mock data imports with API calls
- **ProjectCard.jsx**: No changes needed (receives props)
- **ServiceCard.jsx**: No changes needed (receives props)
- **Header.jsx**: No changes needed (receives props)

### 3. Add State Management
- Use React hooks (useState, useEffect) for data fetching
- Add loading states for better UX
- Handle error states gracefully

### 4. Data Transformation
- Ensure backend data matches frontend expectations
- Map MongoDB `_id` to frontend `id` field
- Handle any data structure differences

## Implementation Steps

1. **Backend Development**:
   - Create MongoDB models
   - Implement CRUD endpoints
   - Seed database with mock data
   - Test API endpoints

2. **Frontend Integration**:
   - Create API service layer
   - Update App.js to fetch data from backend
   - Remove mock.js dependency
   - Add loading and error handling

3. **Testing**:
   - Test all API endpoints
   - Test frontend integration
   - Verify all sections display correctly

## Error Handling
- Backend: Return consistent error responses with status codes
- Frontend: Display user-friendly error messages
- Fallback to loading states during API calls

## Notes
- All data will be seeded from current mock.js structure
- Frontend components remain unchanged (props-based)
- Maintain same color scheme and layout
- Add loading states for better UX