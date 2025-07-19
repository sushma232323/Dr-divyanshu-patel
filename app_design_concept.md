# Dr. Divyanshu – 5D Integrative Health App Design Concept

## Overview
A comprehensive mobile health application that integrates Ayurveda, Naturopathy, Acupuncture, Nutrition, and modern medical practices under one platform.

## Visual Style
- **Theme**: Professional Dark Mode with healing green accents
- **Primary Colors**: 
  - Background: Deep charcoal (#1A1A1A)
  - Surface: Dark gray (#2D2D2D)
  - Primary: Healing green (#4CAF50)
  - Accent: Golden yellow (#FFC107)
  - Text: White (#FFFFFF) and light gray (#E0E0E0)

## Typography
- **Primary Font**: Roboto (clean, medical-grade readability)
- **Secondary Font**: Noto Sans (for Hindi/Sanskrit terms)
- **Hierarchy**: 
  - Headers: 24sp, Bold
  - Subheaders: 18sp, Medium
  - Body: 16sp, Regular
  - Captions: 14sp, Light

## Iconography
- Medical and health-focused icons
- Ayurvedic symbols (lotus, chakras, herbs)
- Modern minimalist style
- Consistent stroke width and corner radius

## Layout Principles
- **Grid System**: 8dp grid for consistent spacing
- **Card-based Design**: Each module as a distinct card
- **Bottom Navigation**: Easy thumb access for main sections
- **Floating Action Button**: Quick access to consultation booking

## User Experience Flow
1. **Splash Screen**: Dr. Divyanshu branding with healing animation
2. **Home Dashboard**: 10 module tiles in grid layout
3. **Module Pages**: Consistent layout with content, images, and actions
4. **Consultation Flow**: Multi-step form with WhatsApp integration
5. **Content Pages**: Rich text, images, and interactive elements

## Accessibility
- High contrast ratios for dark mode
- Large touch targets (minimum 48dp)
- Screen reader compatibility
- Font scaling support

## Technical Specifications
- **Framework**: Flutter
- **Platform**: Android (with iOS compatibility)
- **Minimum SDK**: Android 21 (Lollipop)
- **Target SDK**: Android 34
- **Architecture**: Clean Architecture with BLoC pattern
- **State Management**: Flutter BLoC
- **Navigation**: Go Router
- **Local Storage**: Hive/SQLite
- **Network**: Dio for HTTP requests
- **Image Loading**: Cached Network Image

## Module Structure
Each of the 10 modules will follow a consistent design pattern:
1. **Header**: Module icon, title, and brief description
2. **Content Area**: Scrollable content with rich media
3. **Action Buttons**: Primary actions (book consultation, download, etc.)
4. **Related Links**: Cross-module navigation

## Dark Mode Implementation
- System-aware theme switching
- Manual toggle option in settings
- Consistent color palette across all screens
- Optimized for OLED displays to save battery

