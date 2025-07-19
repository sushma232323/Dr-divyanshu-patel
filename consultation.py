from flask import Blueprint, request, jsonify
from datetime import datetime
import uuid
from src.services.google_sheets_service import google_sheets_service

consultation_bp = Blueprint('consultation', __name__)

@consultation_bp.route('/consultations', methods=['POST'])
def submit_consultation():
    """Submit a new consultation request."""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'phone', 'email', 'age', 'gender', 'medicalConditions', 'consultationType', 'date', 'time']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({
                    'success': False,
                    'message': f'Missing required field: {field}'
                }), 400
        
        # Generate unique ID and timestamp
        consultation_id = str(uuid.uuid4())
        created_at = datetime.now().isoformat()
        
        # Prepare consultation data
        consultation_data = {
            'id': consultation_id,
            'name': data['name'],
            'phone': data['phone'],
            'email': data['email'],
            'age': int(data['age']),
            'gender': data['gender'],
            'medicalConditions': data['medicalConditions'],
            'consultationType': data['consultationType'],
            'date': data['date'],
            'time': data['time'],
            'createdAt': created_at,
            'status': 'pending'
        }
        
        # Submit to Google Sheets
        success = google_sheets_service.append_consultation_data(consultation_data)
        
        if success:
            return jsonify({
                'success': True,
                'message': 'Consultation request submitted successfully',
                'consultationId': consultation_id
            }), 201
        else:
            return jsonify({
                'success': False,
                'message': 'Failed to submit consultation request'
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error processing request: {str(e)}'
        }), 500

@consultation_bp.route('/consultations', methods=['GET'])
def get_consultations():
    """Get all consultation requests."""
    try:
        consultations = google_sheets_service.get_consultation_data()
        
        return jsonify({
            'success': True,
            'data': consultations,
            'count': len(consultations)
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error retrieving consultations: {str(e)}'
        }), 500

@consultation_bp.route('/consultations/<consultation_id>/status', methods=['PUT'])
def update_consultation_status(consultation_id):
    """Update the status of a consultation request."""
    try:
        data = request.get_json()
        
        if 'status' not in data:
            return jsonify({
                'success': False,
                'message': 'Missing status field'
            }), 400
        
        valid_statuses = ['pending', 'confirmed', 'completed', 'cancelled']
        if data['status'] not in valid_statuses:
            return jsonify({
                'success': False,
                'message': f'Invalid status. Must be one of: {valid_statuses}'
            }), 400
        
        success = google_sheets_service.update_consultation_status(consultation_id, data['status'])
        
        if success:
            return jsonify({
                'success': True,
                'message': 'Consultation status updated successfully'
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': 'Failed to update consultation status'
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error updating status: {str(e)}'
        }), 500

@consultation_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'success': True,
        'message': 'Dr. Divyanshu Health API is running',
        'timestamp': datetime.now().isoformat()
    }), 200

@consultation_bp.route('/whatsapp/webhook', methods=['POST'])
def whatsapp_webhook():
    """Handle WhatsApp webhook for bot integration."""
    try:
        data = request.get_json()
        
        # Log the webhook data (in production, you'd process this properly)
        print(f"WhatsApp webhook received: {data}")
        
        # Basic webhook verification
        if 'message' in data and 'from' in data:
            # Process the message
            message = data['message']
            sender = data['from']
            
            # Simple auto-response logic
            if 'book' in message.lower() or 'appointment' in message.lower():
                response_message = f"Hello! Thank you for contacting Dr. Divyanshu. To book an appointment, please use our mobile app or call {'+91 9695570344'}."
            else:
                response_message = "Hello! For health consultations and appointments, please use our mobile app or contact us at +91 9695570344."
            
            return jsonify({
                'success': True,
                'response': response_message,
                'to': sender
            }), 200
        
        return jsonify({
            'success': True,
            'message': 'Webhook received'
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Webhook error: {str(e)}'
        }), 500

