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

RapidTriage is a full-stack mobile application designed to provide real-time, AI-driven medical triage assessments and help users locate nearby healthcare facilities during emergencies. The app employs a **hybrid AI approach** combining large language models (LLMs) with clinically validated rules-based triage frameworks (Manchester Triage System/ESI) to deliver accurate, standardized urgency classifications.

**Academic Context**: This project was developed for **CS 5100 - Artificial Intelligence** (Spring 2025) at Northeastern University, demonstrating the intersection of healthcare, mobile computing, and artificial intelligence.

### Problem Statement

Emergency departments face significant challenges due to high loads of non-urgent visits and symptom ambiguity:

1. **Symptom Ambiguity**: Many individuals struggle to clearly articulate symptoms (e.g., "I feel off"), leading to:
   - Under-reporting of serious conditions
   - Overuse of emergency services for non-urgent cases
   - Difficulty in self-assessing urgency levels

2. **Lack of Accessible Self-Assessment Tools**: Limited availability of real-time triage tools that combine:
   - Natural language understanding for vague inputs
   - Clinical validation through standardized frameworks
   - Fast response times suitable for emergency scenarios

3. **Emergency Room Load Balancing**: Need for tools that help users make informed decisions before arriving at hospitals

### Solution: Hybrid AI Triage System

RapidTriage addresses these challenges through a unique **hybrid AI architecture**:

- 🤖 **LLM-Driven Symptom Parsing**: Fine-tuned language models interpret vague user inputs and ask clarifying questions iteratively
- 📋 **Rules-Based Triage Engine**: Structured outputs flow into clinically validated frameworks (Manchester Triage/ESI) for standardized urgency classification
- ⚡ **Real-Time Performance**: Sub-5-second response times (~3.7 seconds average) for immediate decision support
- 🎯 **False Positive Mitigation**: Continuous monitoring and threshold calibration to reduce unnecessary hospital alerts
- 🎤 **Multi-Modal Input**: Support for both text and voice input for maximum accessibility
- 📍 **Location Intelligence**: Real-time hospital discovery with distance and rating sorting
- 🗺️ **Interactive Maps**: Visual hospital locations with one-tap directions and calling

## 🎬 Demo

### Project Documentation

Comprehensive project documentation including progress reports, final reports, and detailed methodology can be found in the `docs/images/` directory.

![Project Progress Report](docs/images/progress_report_thumbnail.png)

*Project Progress Report - RapidTriage AI (CS 5100, Spring 2025)*

### App Screenshots
<!-- 
![Home Screen](screenshots/home.png)
![Assessment Screen](screenshots/assessment.png)
![Hospital Finder](screenshots/hospitals.png)
![Results Screen](screenshots/results.png)
-->

### Live Demo
<!-- Add links to Expo Go, web demo, or app store links -->

---

## 👥 Team

**Course**: CS 5100 - Artificial Intelligence | **Semester**: Spring 2025 | **Institution**: Northeastern University

- **Kaustubha Venkata Eluri** - Mobile UI, LLM integration, testing & presentation
- **Yadhukrishnan Pankajakshan** - Backend logic, rule engine, API and alert system

## ✨ Key Features

### 🩺 Hybrid AI Triage System
- **Iterative Symptom Querying**: LLM asks clarifying questions when inputs are incomplete or ambiguous (e.g., "How long have you felt this symptom?", "What is the severity?")
- **Clinically Validated Frameworks**: Integration with Manchester Triage System (MTS) and Emergency Severity Index (ESI) for standardized urgency classification
- **Multi-Provider AI Support**: Integration with OpenAI GPT, Anthropic Claude, and Google Gemini with intelligent fallback mechanisms
- **Structured Output Mapping**: LLM outputs are mapped to structured data (symptom, severity, location, duration) for rules-based classification
- **Real-Time Performance**: Average response time of ~3.7 seconds (under 5 seconds target)
- **Accuracy Metrics**: 85-92% accuracy based on synthetic test cases across different symptom categories
- **False Positive Monitoring**: Continuous tracking and threshold calibration to minimize unnecessary hospital alerts

### 🎤 Advanced Voice Processing
- **High-Quality Audio Capture**: Professional-grade audio recording using Expo AV
- **Automatic Transcription**: Seamless conversion of voice recordings to text for LLM analysis
- **Visual Feedback**: Real-time recording indicators and intuitive controls
- **Cross-Platform Support**: Works seamlessly on iOS, Android, and Web

### 🏥 Smart Hospital Discovery
- **Location-Based Search**: Automatic detection of nearby hospitals using device GPS
- **Intelligent Sorting**: Sort by rating, distance, or a combination of both
- **Interactive Maps**: Full-featured map integration with React Native Maps
- **Quick Actions**: One-tap access to directions, hospital calling, and emergency services
- **Critical Case Alerts**: Automatic hospital notification for cases classified as critical
- **Google Places Integration**: Leverages Google Places API for comprehensive hospital data

### 🏗️ Architecture Highlights
- **Hybrid AI Architecture**: Combines LLM flexibility with structured rules-based logic
- **Full-Stack Solution**: React Native frontend with Go backend service
- **Microservices Architecture**: Modular backend with separate AI provider integrations
- **RESTful API Design**: Clean API endpoints for emergency triage operations
- **Session-Based Privacy**: Secure handling of sensitive medical information
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
- **Hybrid AI Innovation**: Successfully combined LLM flexibility with clinical validation frameworks

## 📊 Results & Performance Metrics

### System Performance

| Metric | Value |
|--------|-------|
| **Average Response Time** | ~3.7 seconds |
| **Target Response Time** | < 5 seconds |
| **Overall Accuracy** | 85-92% |
| **False Positive Rate** | Monitored and minimized through threshold calibration |

### Sample Test Results

| Symptom Reported | Clarifying Questions | Triage Level | Time to Decision | False Positive? |
|------------------|---------------------|--------------|------------------|-----------------|
| Chest pain + dizziness | Yes (2 Qs) | Very Urgent | 4.1 sec | No |
| Mild stomach ache | No | Non-Urgent | 3.0 sec | No |
| Sharp headache | Yes (1 Q) | Urgent | 3.7 sec | No |
| Pain in leg, can't walk | No | Urgent | 3.2 sec | No |
| Light discomfort, unsure | Yes (2 Qs) | Critical | 4.5 sec | Yes |

### Accuracy by Symptom Category

- **Chest Pain**: 92% accuracy
- **Stomach Ache**: 88% accuracy
- **Headache**: 85% accuracy
- **Leg Pain**: 90% accuracy
- **Light Discomfort**: 80% accuracy (improved through iterative questioning)

### Methodology

1. **LLM Fine-Tuning**: Fine-tuned GPT-based models on medical triage data to recognize typical expressions and prompt for missing details
2. **Rules-Based Triage Engine**: Manchester Triage System (MTS) or Emergency Severity Index (ESI) classify cases into urgency levels (Immediate, Very Urgent, Urgent, Non-Urgent)
3. **Iterative Question Subroutine**: LLM detects incomplete information and queries for more details (severity, location, duration)
4. **False Positive Management**: Continuous tracking and iterative threshold calibration to balance caution with efficiency

### Workflow

```
User Input → LLM Clarification → Rule Engine → Triage Output → Hospital Alerts (if critical)
```

### Project Documentation

The following documents provide detailed information about the project's methodology, results, and implementation:

![Project Progress Report](docs/images/progress_report_thumbnail.png)

*Figure 1: Project Progress Report - RapidTriage AI (CS 5100, Spring 2025)*

**Key highlights from the reports:**
- Detailed methodology combining LLM and rules-based triage systems
- Performance metrics and accuracy analysis
- False positive monitoring and threshold calibration
- System architecture and workflow diagrams
- Team contributions and implementation details

> **Note**: Full project reports are available in the repository. For higher quality images or specific diagrams, refer to the original PDF documents.

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

- **Hybrid AI Architecture**: Combining LLM flexibility with rules-based clinical frameworks (Manchester Triage System, ESI)
- **Medical Triage Systems**: Understanding clinically validated triage protocols and their implementation
- **Iterative Questioning Systems**: Designing LLM prompts that ask clarifying questions for incomplete inputs
- **False Positive Management**: Implementing monitoring and threshold calibration systems
- **Full-Stack Development**: Integrating React Native frontend with Go backend
- **Multi-AI Provider Integration**: Working with OpenAI, Claude, and Gemini APIs with fallback mechanisms
- **Cross-Platform Development**: Building apps that work seamlessly across iOS, Android, and Web
- **Real-Time Features**: Implementing GPS tracking, audio recording, and live map updates with sub-5-second response times
- **API Design**: Creating RESTful APIs with proper error handling and status codes
- **State Management**: Managing complex application state with React hooks
- **Performance Optimization**: Optimizing audio processing, map rendering, and LLM inference times
- **User Experience**: Designing intuitive interfaces for emergency scenarios
- **Clinical Validation**: Ensuring AI outputs align with medical standards and protocols

## 🚀 Future Enhancements

Based on project reports and identified areas for improvement:

### Model & Accuracy Improvements
- [ ] **Enhanced Fine-Tuning**: Incorporate real-world or larger simulated patient logs to refine symptom parsing capabilities
- [ ] **False Positive Optimization**: Systematically evaluate borderline cases, refining triage thresholds
- [ ] **Dataset Expansion**: Expand training data with diverse symptom presentations
- [ ] **On-Device LLM**: Investigate model distillation to maintain performance while lowering computational costs

### User Experience
- [ ] **UI/UX Improvements**: Make clarifying question prompts more intuitive (e.g., short yes/no follow-ups for speed)
- [ ] **Offline Mode**: Cache hospital data and enable offline triage assessments
- [ ] **Multi-Language Support**: Internationalization for global accessibility
- [ ] **Dark Mode**: Enhanced UI with dark theme support
- [ ] **Accessibility**: Improved screen reader support and accessibility features

### Integration & Features
- [ ] **Hospital Integration**: Direct integration with hospital systems for seamless alert handling
- [ ] **User Profiles**: Save medical history and preferences
- [ ] **Push Notifications**: Reminders and emergency alerts
- [ ] **Telemedicine Integration**: Connect with healthcare providers directly
- [ ] **Medical Records**: Integration with health record systems

### Technical
- [ ] **Advanced Analytics**: Track triage accuracy and user patterns
- [ ] **Unit & Integration Tests**: Comprehensive test coverage
- [ ] **Scalability**: Optimize for high-volume usage and concurrent requests
- [ ] **Performance Monitoring**: Real-time performance tracking and alerting

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📚 References & Documentation

### Project Reports
- **Progress Report**: RapidTriage AI – Progress Report (CS 5100, Spring 2025)
- **Final Report**: RapidTriage AI – Final Project Report (CS 5100, Spring 2025)

### Literature Review
This project builds upon research in:
- **LLM for Medical Triage**: GPT-based models for parsing free-text medical complaints
- **Rules-Based Triage Systems**: Manchester Triage System (MTS) and Emergency Severity Index (ESI) protocols
- **Hybrid AI in Medical Decision-Making**: Combining LLM-driven parsing with rules-based engines
- **BERT for Symptom Extraction**: T. M. Nguyen et al., 2021
- **Deep Learning in Medical Imaging**: K. Rajpurkar et al., 2018 (CheXNet)
- **Manchester Triage Group**, 2006: Standardized triage logic and guidelines

### Clinical Frameworks
- **Manchester Triage System (MTS)**: Five-level triage system used in emergency departments
- **Emergency Severity Index (ESI)**: Five-level triage algorithm for emergency departments

## 📧 Contact & Support

- **Issues**: [GitHub Issues](link-to-issues)
- **Email**: [Your Email]
- **Portfolio**: [Your Portfolio Link]
- **LinkedIn**: [Your LinkedIn]

---

<div align="center">

**Built with ❤️ using React Native, Go, and AI**

**CS 5100 - Artificial Intelligence | Spring 2025 | Northeastern University**

⭐ Star this repo if you find it helpful!

</div>
