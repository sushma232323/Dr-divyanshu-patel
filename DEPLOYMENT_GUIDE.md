# 📱 Dr. Divyanshu Health App - Deployment Guide

## 🎯 Quick Start

This guide will help you build and deploy the **Dr. Divyanshu – 5D Integrative Health** mobile application.

## 📋 Prerequisites Checklist

### Required Software
- [ ] **Flutter SDK** (3.5.4+) - [Download](https://flutter.dev/docs/get-started/install)
- [ ] **Android Studio** - [Download](https://developer.android.com/studio)
- [ ] **Java JDK** (11+) - [Download](https://adoptium.net/)
- [ ] **Git** - [Download](https://git-scm.com/)

### System Requirements
- **OS**: Windows 10+, macOS 10.14+, or Linux
- **RAM**: 8GB minimum, 16GB recommended
- **Storage**: 10GB free space
- **Internet**: Required for initial setup

## 🛠️ Step-by-Step Setup

### 1. Install Flutter
```bash
# Download Flutter SDK
git clone https://github.com/flutter/flutter.git -b stable
export PATH="$PATH:`pwd`/flutter/bin"

# Verify installation
flutter doctor
```

### 2. Setup Android Development
```bash
# Install Android Studio
# During installation, ensure these components are selected:
# - Android SDK
# - Android SDK Platform-Tools
# - Android SDK Build-Tools
# - Android SDK Command-line Tools

# Accept Android licenses
flutter doctor --android-licenses
```

### 3. Clone and Setup Project
```bash
# Clone the project
git clone <project-repository>
cd dr_divyanshu_health_app

# Install dependencies
flutter pub get

# Verify setup
flutter doctor
```

## 🔨 Building the Application

### Debug Build (for Testing)
```bash
# Build debug APK
flutter build apk --debug

# Install on connected device
flutter install
```

### Release Build (for Distribution)
```bash
# Build release APK
flutter build apk --release

# Build optimized APKs for different architectures
flutter build apk --split-per-abi --release
```

### App Bundle (for Google Play Store)
```bash
# Build App Bundle
flutter build appbundle --release
```

## 📦 Output Files

After successful build, you'll find:

### APK Files
```
build/app/outputs/flutter-apk/
├── app-release.apk (Universal APK - ~50MB)
├── app-arm64-v8a-release.apk (64-bit ARM - ~25MB)
├── app-armeabi-v7a-release.apk (32-bit ARM - ~23MB)
└── app-x86_64-release.apk (64-bit Intel - ~27MB)
```

### App Bundle
```
build/app/outputs/bundle/release/
└── app-release.aab (For Google Play Store)
```

## 🚀 Distribution Methods

### Method 1: Direct APK Installation

**Best for**: Beta testing, internal distribution

1. **Share APK File**
   - Use `app-release.apk` for universal compatibility
   - Or use specific architecture APKs for smaller file size

2. **Installation Instructions for Users**
   ```
   1. Download the APK file
   2. Go to Settings > Security > Unknown Sources
   3. Enable "Install from Unknown Sources"
   4. Open the APK file and install
   ```

### Method 2: Google Play Store

**Best for**: Public distribution

1. **Prepare App Bundle**
   - Use `app-release.aab` file
   - File size: ~15-20MB (optimized by Google Play)

2. **Google Play Console Setup**
   - Create developer account ($25 one-time fee)
   - Upload app bundle
   - Complete store listing
   - Submit for review

3. **Store Listing Requirements**
   - App icon (512x512 PNG)
   - Screenshots (phone and tablet)
   - Feature graphic (1024x500)
   - App description
   - Privacy policy URL

### Method 3: Alternative App Stores

**Options**: Amazon Appstore, Samsung Galaxy Store, Huawei AppGallery

## 🔧 Backend Deployment

### Local Backend Setup
```bash
cd dr_divyanshu_backend
source venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

### Cloud Deployment Options

#### Option 1: Heroku (Free Tier Available)
```bash
# Install Heroku CLI
# Create Procfile in backend directory
echo "web: python src/main.py" > Procfile

# Deploy
heroku create dr-divyanshu-backend
git push heroku main
```

#### Option 2: Google Cloud Platform
```bash
# Create app.yaml for App Engine
gcloud app deploy
```

#### Option 3: AWS EC2
```bash
# Use AWS EC2 instance with Ubuntu
# Install Python, pip, and dependencies
# Run with gunicorn for production
```

## 📊 Google Sheets Integration

### Setup Steps
1. **Create Google Cloud Project**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create new project: "Dr Divyanshu Health App"

2. **Enable APIs**
   - Enable Google Sheets API
   - Enable Google Drive API

3. **Create Service Account**
   - Go to IAM & Admin > Service Accounts
   - Create service account: "health-app-service"
   - Download JSON key file

4. **Setup Google Sheet**
   - Create new Google Sheet: "Consultation Data"
   - Share with service account email
   - Copy sheet ID from URL

5. **Configure Backend**
   - Place JSON key file in backend directory
   - Update `google_sheets_service.py` with credentials
   - Update sheet ID in configuration

## 🔐 Security Configuration

### App Signing (for Release)
```bash
# Generate keystore
keytool -genkey -v -keystore dr-divyanshu-key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias dr-divyanshu

# Configure in android/app/build.gradle
```

### API Security
- Use HTTPS for all API calls
- Implement API key authentication
- Enable CORS for web access
- Use environment variables for secrets

## 📱 Testing Checklist

### Pre-Release Testing
- [ ] App installs successfully
- [ ] All 10 modules load correctly
- [ ] Consultation form submits data
- [ ] WhatsApp integration works
- [ ] E-books download properly
- [ ] Dark mode displays correctly
- [ ] Navigation between screens works
- [ ] Backend API responds correctly

### Device Testing
- [ ] Android 8.0+ compatibility
- [ ] Different screen sizes (phone/tablet)
- [ ] Various Android manufacturers
- [ ] Network connectivity issues
- [ ] Offline functionality

## 🚨 Troubleshooting

### Common Build Issues

#### "Android SDK not found"
```bash
export ANDROID_HOME=/path/to/android-sdk
export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin
flutter doctor
```

#### "Gradle build failed"
```bash
cd android
./gradlew clean
cd ..
flutter clean
flutter pub get
flutter build apk
```

#### "Java version incompatible"
```bash
# Install Java 11
sudo apt install openjdk-11-jdk
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

### Runtime Issues

#### "Network error"
- Check internet connection
- Verify backend URL in app configuration
- Ensure CORS is enabled on backend

#### "WhatsApp not opening"
- Verify WhatsApp is installed
- Check phone number format
- Test URL format: `https://wa.me/919695570344`

## 📈 Performance Optimization

### APK Size Reduction
```bash
# Enable R8 obfuscation
flutter build apk --release --obfuscate --split-debug-info=debug-info/

# Use split APKs
flutter build apk --split-per-abi --release
```

### App Performance
- Enable tree shaking for unused code
- Optimize images and assets
- Use lazy loading for modules
- Implement caching for API responses

## 📞 Support & Maintenance

### Monitoring
- Set up crash reporting (Firebase Crashlytics)
- Monitor API performance
- Track user engagement
- Monitor app store reviews

### Updates
- Regular security updates
- Feature enhancements based on user feedback
- Bug fixes and performance improvements
- Medical content updates

## 🎯 Launch Strategy

### Soft Launch
1. **Internal Testing** (1 week)
   - Team members and close contacts
   - Test all features thoroughly
   - Fix critical bugs

2. **Beta Testing** (2 weeks)
   - Limited user group (50-100 users)
   - Gather feedback and analytics
   - Optimize based on usage patterns

3. **Public Launch**
   - Google Play Store submission
   - Marketing and promotion
   - User support setup

### Marketing Materials
- App store screenshots
- Feature highlight videos
- Social media content
- Press release for health community

---

## 📋 Final Checklist

Before going live, ensure:
- [ ] All features tested and working
- [ ] Backend deployed and stable
- [ ] Google Sheets integration configured
- [ ] App signed with release key
- [ ] Store listing completed
- [ ] Privacy policy published
- [ ] Support channels established
- [ ] Analytics and monitoring setup
- [ ] Backup and recovery plan ready

---

**🎉 Congratulations! Your Dr. Divyanshu Health App is ready for deployment!**

For technical support during deployment, refer to the main README.md or contact the development team.

