# 🏥 RapidTriage

<div align="center">

**A cross-platform medical triage application that leverages AI to help users assess symptoms and find nearby hospitals in emergency situations.**

[![React Native](https://img.shields.io/badge/React%20Native-0.76.9-61DAFB?logo=react&logoColor=white)](https://reactnative.dev/)
[![Expo](https://img.shields.io/badge/Expo-52.0.46-000020?logo=expo&logoColor=white)](https://expo.dev/)
[![Go](https://img.shields.io/badge/Go-1.23-00ADD8?logo=go&logoColor=white)](https://golang.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.3-blue?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)

[Demo](#-demo) • [Features](#-key-features) • [Tech Stack](#-tech-stack) • [Installation](#-installation)

</div>

---

## 📖 About

RapidTriage is a full-stack mobile application designed to provide quick medical triage assessments and help users locate nearby healthcare facilities during emergencies. The app combines **AI-powered symptom analysis** with **real-time location services** to deliver a comprehensive emergency medical assistance solution.

### Problem Statement

During medical emergencies, people often struggle with:
- **Uncertainty** about symptom severity and urgency
- **Difficulty** finding nearby hospitals quickly
- **Lack of access** to immediate medical guidance
- **Time-sensitive decisions** that could impact outcomes

RapidTriage addresses these challenges by providing instant AI-powered triage assessments and seamless hospital discovery.

### Solution

- 🤖 **AI-Powered Triage**: Multi-provider AI integration (OpenAI, Claude, Gemini) for accurate symptom analysis
- 🎤 **Voice & Text Input**: Flexible input methods for accessibility and convenience
- 📍 **Location Intelligence**: Real-time hospital discovery with distance and rating sorting
- 🗺️ **Interactive Maps**: Visual hospital locations with one-tap directions and calling
- ⚡ **Fast Response**: Optimized for quick decision-making in emergency scenarios

## 🎬 Demo

<!-- Add screenshots or demo video here -->
> **Note**: Add screenshots or a demo video link here to showcase the app in action.

### Screenshots
<!-- 
![Home Screen](screenshots/home.png)
![Assessment Screen](screenshots/assessment.png)
![Hospital Finder](screenshots/hospitals.png)
![Results Screen](screenshots/results.png)
-->

### Live Demo
<!-- Add links to Expo Go, web demo, or app store links -->

---

## ✨ Key Features

### 🩺 Intelligent Symptom Assessment
- **Multi-Modal Input**: Support for both text and voice input for maximum accessibility
- **Comprehensive Data Collection**: Duration tracking, pain level rating, and detailed symptom descriptions
- **AI-Powered Analysis**: Integration with multiple AI providers (OpenAI GPT, Anthropic Claude, Google Gemini) for accurate triage classification
- **Real-Time Results**: Instant assessment with severity classification and recommendations

### 🎤 Advanced Voice Processing
- **High-Quality Audio Capture**: Professional-grade audio recording using Expo AV
- **Automatic Transcription**: Seamless conversion of voice recordings to text for analysis
- **Visual Feedback**: Real-time recording indicators and intuitive controls
- **Cross-Platform Support**: Works seamlessly on iOS, Android, and Web

### 🏥 Smart Hospital Discovery
- **Location-Based Search**: Automatic detection of nearby hospitals using device GPS
- **Intelligent Sorting**: Sort by rating, distance, or a combination of both
- **Interactive Maps**: Full-featured map integration with React Native Maps
- **Quick Actions**: One-tap access to directions, hospital calling, and emergency services
- **Google Places Integration**: Leverages Google Places API for comprehensive hospital data

### 🏗️ Architecture Highlights
- **Full-Stack Solution**: React Native frontend with Go backend service
- **Microservices Architecture**: Modular backend with separate AI provider integrations
- **RESTful API Design**: Clean API endpoints for emergency triage operations
- **Environment-Based Configuration**: Flexible configuration for development and production

## 🎯 Key Highlights

- ✅ **Full-Stack Development**: Built both frontend (React Native) and backend (Go) from scratch
- ✅ **Multi-AI Integration**: Implemented support for 3 different AI providers with fallback mechanisms
- ✅ **Cross-Platform**: Single codebase supporting iOS, Android, and Web platforms
- ✅ **Real-Time Features**: GPS-based location services, audio recording, and live map updates
- ✅ **Production-Ready**: Environment-based configuration, error handling, and API integration
- ✅ **Modern Architecture**: Modular design with separation of concerns and reusable components
- ✅ **API Integration**: RESTful API design with Google Places API integration
- ✅ **User Experience**: Intuitive UI with haptic feedback, animations, and accessibility features

## 🏆 Technical Achievements

- **Scalable Architecture**: Designed a modular backend that can easily integrate additional AI providers
- **Performance Optimization**: Efficient audio processing and map rendering for smooth user experience
- **Error Handling**: Comprehensive error handling and user feedback mechanisms
- **Code Quality**: TypeScript support, ESLint configuration, and clean code practices
- **API Design**: RESTful endpoints with proper status codes and error responses

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** (v18 or higher)
- **npm** or **yarn**
- **Expo CLI** (`npm install -g expo-cli`)
- **Go** (v1.23 or higher) - for backend development
- **Google Places API Key** - for hospital finder functionality

## 🚀 Quick Start

Get RapidTriage up and running in minutes:

```bash
# Clone the repository
git clone <repository-url>
cd RapidTriage

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# Start the development server
npm start
```

## 🛠️ Installation

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd RapidTriage
```

### Step 2: Install Dependencies

```bash
npm install
```

For backend dependencies:
```bash
cd agent
go mod download
```

### Step 3: Configure Environment Variables

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` and configure your settings:

```env
# Backend API Base URL
API_BASE_URL=http://localhost:8080/api/v1

# Google Places API Key (required for hospital finder)
GOOGLE_PLACES_API_KEY=your_google_places_api_key_here

# Environment
NODE_ENV=development
```

#### 🔑 Getting API Keys

**Google Places API Key:**
1. Visit [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the **Places API**
4. Navigate to **Credentials** → **Create Credentials** → **API Key**
5. Restrict the API key to **Places API** for security
6. Copy the key to your `.env` file

**Backend API:**
- The backend runs locally by default at `http://localhost:8080/api/v1`
- For production, update `API_BASE_URL` to your deployed backend URL

### Step 4: Start Development Servers

**Frontend (Terminal 1):**
```bash
npm start
```

This starts the Expo development server. Options:
- Press `i` → Open iOS simulator
- Press `a` → Open Android emulator  
- Scan QR code → Open in Expo Go app on your phone
- Press `w` → Open in web browser

**Backend (Terminal 2):**
```bash
cd agent
go run cmd/server/main.go
```

The backend API will be available at `http://localhost:8080/api/v1`

## 🏃 Running the App

### Mobile Development

```bash
# iOS
npm run ios

# Android
npm run android

# Web
npm run web
```

### Backend Server

The backend is a Go service located in the `agent/` directory:

```bash
cd agent
go run cmd/server/main.go
```

The backend API will be available at `http://localhost:8080/api/v1`

## 🏗️ Project Structure

```
RapidTriage/
├── agent/                 # Go backend service
│   ├── cmd/server/       # Server entry point
│   ├── internal/         # Internal packages
│   │   ├── ai/          # AI provider integrations
│   │   ├── api/         # API handlers
│   │   ├── config/      # Configuration
│   │   ├── models/      # Data models
│   │   ├── tools/       # Tool integrations
│   │   └── triage/      # Triage classification logic
│   └── go.mod           # Go dependencies
├── src/
│   ├── components/      # React Native components
│   ├── screens/        # App screens
│   ├── services/       # API and service integrations
│   └── utils/          # Utility functions and config
├── assets/             # Images, fonts, and other assets
└── package.json        # Node.js dependencies
```

## 🛠️ Tech Stack

### Frontend Technologies
| Category | Technology | Purpose |
|----------|-----------|---------|
| **Framework** | React Native 0.76.9 | Cross-platform mobile development |
| **Platform** | Expo ~52.0.46 | Development tooling and deployment |
| **Navigation** | React Navigation 7.x | Screen routing and navigation |
| **Audio** | Expo AV 15.x | Voice recording and playback |
| **Maps** | React Native Maps 1.22 | Interactive map visualization |
| **HTTP Client** | Axios 1.8 | API communication |
| **Location** | Expo Location 18.x | GPS and location services |
| **State Management** | React Hooks | Component state management |

### Backend Technologies
| Category | Technology | Purpose |
|----------|-----------|---------|
| **Language** | Go 1.23 | High-performance backend service |
| **AI Providers** | OpenAI API | GPT-based symptom analysis |
| **AI Providers** | Anthropic Claude | Alternative AI analysis |
| **AI Providers** | Google Gemini | Multi-provider fallback |
| **Architecture** | RESTful API | Clean API design |

### Key Libraries & Tools
- **@react-native-community/geolocation** - Location services
- **@react-native-community/slider** - UI components
- **expo-blur** - Visual effects
- **expo-haptics** - Tactile feedback
- **react-native-gesture-handler** - Gesture recognition
- **react-native-reanimated** - Smooth animations

## 🔌 Backend Integration

RapidTriage uses a Go-based backend service for AI-powered triage analysis. The backend architecture supports multiple AI providers with intelligent fallback mechanisms.

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/health` | Health check endpoint |
| `POST` | `/api/v1/emergency/text` | Text-based symptom triage analysis |
| `POST` | `/api/v1/emergency` | Voice/audio-based triage analysis |

### Backend Architecture

```
agent/
├── cmd/server/          # Server entry point
├── internal/
│   ├── ai/             # AI provider integrations (OpenAI, Claude, Gemini)
│   ├── api/            # HTTP handlers and middleware
│   ├── config/         # Configuration management
│   ├── models/         # Data models and structures
│   ├── tools/          # Tool integrations (ambulance, booking, hospital)
│   └── triage/         # Triage classification logic
```

### Connecting to Backend

1. **Local Development**: Backend runs on `http://localhost:8080/api/v1` by default
2. **Production**: Update `API_BASE_URL` in `.env` to your production endpoint
3. **Authentication**: Add authentication headers in `src/services/ChatService.js` if required

## 📱 Permissions

The app requires the following permissions:

- **Microphone** - For voice recording
- **Location** - For finding nearby hospitals

These are automatically requested when needed. Permissions are configured in `app.json`.

## 🧪 Testing

```bash
npm test
```

## 🐛 Troubleshooting

### Common Issues

**Issue**: Expo Go app can't connect to development server
- **Solution**: Ensure your phone and computer are on the same Wi-Fi network

**Issue**: Google Places API not working
- **Solution**: Verify your API key is correct and has Places API enabled

**Issue**: Backend connection errors
- **Solution**: Ensure the backend server is running and `API_BASE_URL` in `.env` is correct

**Issue**: Audio recording not working
- **Solution**: Grant microphone permissions in your device settings

## 📝 Development

### Available Scripts

| Command | Description |
|---------|-------------|
| `npm start` | Start Expo development server |
| `npm run ios` | Run on iOS simulator |
| `npm run android` | Run on Android emulator |
| `npm run web` | Run in web browser |
| `npm run lint` | Run ESLint for code quality |
| `npm test` | Run test suite |

### Code Quality

- **ESLint**: Code linting and style enforcement
- **TypeScript**: Type checking for improved code reliability
- **Prettier**: Code formatting (if configured)
- **Git Hooks**: Pre-commit checks (if configured)

### Project Structure

```
RapidTriage/
├── agent/                      # Go backend service
│   ├── cmd/server/            # Server entry point
│   ├── internal/
│   │   ├── ai/               # AI provider integrations
│   │   ├── api/              # HTTP handlers
│   │   ├── config/           # Configuration
│   │   ├── models/           # Data models
│   │   ├── tools/            # Tool integrations
│   │   └── triage/           # Triage logic
│   └── go.mod                # Go dependencies
├── src/
│   ├── components/           # Reusable React components
│   │   ├── hospitals/       # Hospital-related components
│   │   └── VoiceRecorder.js # Voice recording component
│   ├── screens/             # App screens
│   ├── services/            # API and service integrations
│   └── utils/               # Utility functions
├── assets/                  # Images, fonts, icons
├── constants/              # App constants
└── package.json            # Node.js dependencies
```

## 🎓 What I Learned

Building RapidTriage provided valuable experience in:

- **Full-Stack Development**: Integrating React Native frontend with Go backend
- **AI Integration**: Working with multiple AI providers and implementing fallback strategies
- **Cross-Platform Development**: Building apps that work seamlessly across iOS, Android, and Web
- **Real-Time Features**: Implementing GPS tracking, audio recording, and live map updates
- **API Design**: Creating RESTful APIs with proper error handling and status codes
- **State Management**: Managing complex application state with React hooks
- **Performance Optimization**: Optimizing audio processing and map rendering
- **User Experience**: Designing intuitive interfaces for emergency scenarios

## 🚀 Future Enhancements

Potential improvements and features:

- [ ] **Offline Mode**: Cache hospital data and enable offline triage assessments
- [ ] **Multi-Language Support**: Internationalization for global accessibility
- [ ] **User Profiles**: Save medical history and preferences
- [ ] **Push Notifications**: Reminders and emergency alerts
- [ ] **Telemedicine Integration**: Connect with healthcare providers directly
- [ ] **Medical Records**: Integration with health record systems
- [ ] **Advanced Analytics**: Track triage accuracy and user patterns
- [ ] **Dark Mode**: Enhanced UI with dark theme support
- [ ] **Accessibility**: Improved screen reader support and accessibility features
- [ ] **Unit & Integration Tests**: Comprehensive test coverage

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact & Support

- **Issues**: [GitHub Issues](link-to-issues)
- **Email**: [Your Email]
- **Portfolio**: [Your Portfolio Link]
- **LinkedIn**: [Your LinkedIn]

---

<div align="center">

**Built with ❤️ using React Native, Go, and AI**

⭐ Star this repo if you find it helpful!

</div>
