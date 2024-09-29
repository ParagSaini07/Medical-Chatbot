from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# Medical chatbot logic
class MedicalChatbot:
    def __init__(self):
        # Dictionary with multiple conditions, medications, precautions, and diet suggestions
        self.conditions = {
    'fever': {
        'medications': {
            'paracetamol': {
                'dosage': '500mg every 6 hours',
                'link': 'https://www.onebharatpharmacy.com/product/product_details/911/paracip-500-tablet?srsltid=AfmBOoowBZRJXaVOpqT-CYPFdOJIddc6rWwtXYqjPTE7zKT1bBBZ62kbYrU'
            }
        },
        'precautions': 'Stay hydrated, take rest, avoid cold beverages.',
        'diet': 'Eat light food, drink plenty of fluids, avoid spicy and fried foods.',
        'if_not_working': 'If symptoms persist or worsen (e.g., high fever, trouble breathing), consult a doctor.'
    },
    'cold': {
        'medications': {
            'antihistamine': {
                'dosage': '10mg once daily',
                'link':'https://www.google.com/search?q=antihistamine' 
            },
            'decongestant': {
                'dosage': 'as per need',
                'link': 'https://www.google.com/search?q=decongestant'
            }
        },
        'precautions': 'Keep warm, avoid cold drinks, stay hydrated.',
        'diet': 'Drink warm fluids, eat light soups, avoid dairy products.',
        'if_not_working': 'If the cold persists for more than 10 days or symptoms worsen, consult a doctor.'
    },
    'headache': {
        'medications': {
            'ibuprofen': {
                'dosage': '400mg every 8 hours',
                'link': 'https://www.google.com/search?q=ibuprofen'
            }
        },
        'precautions': 'Avoid bright light, rest in a quiet environment.',
        'diet': 'Stay hydrated, avoid caffeine and processed foods.',
        'if_not_working': 'If the headache becomes severe or persists, consult a doctor.'
    },
    'stomach pain': {
        'medications': {
            'antacid': {
                'dosage': 'as per need',
                'link': 'https://www.google.com/search?q=antacid'
            }
        },
        'precautions': 'Avoid spicy, oily, and acidic foods, eat smaller meals.',
        'diet': 'Eat light and bland foods, avoid fried and fatty foods.',
        'if_not_working': 'If stomach pain persists or worsens, especially with vomiting or fever, consult a doctor.'
    },
    'cough': {
        'medications': {
            'cough syrup': {
                'dosage': 'Take 5ml 2-3 times daily',
                'link': 'https://www.google.com/search?q=cough+syrup'
            }
        },
        'precautions': 'Avoid cold air, drink warm fluids, avoid smoking.',
        'diet': 'Consume warm soups and teas, avoid cold beverages, stay hydrated.',
        'if_not_working': 'If the cough lasts more than 3 weeks or worsens, consult a doctor.'
    },
    'diarrhea': {
        'medications': {
            'oral rehydration salts': {
                'dosage': 'as per need',
                'link': 'https://www.google.com/search?q=oral+rehydration+salts'
            },
            'loperamide': {
                'dosage': 'as directed',
                'link': 'https://www.google.com/search?q=loperamide'
            }
        },
        'precautions': 'Stay hydrated, avoid dehydration, wash hands frequently.',
        'diet': 'Drink electrolyte solutions, eat bananas, rice, applesauce, and toast (BRAT diet). Avoid greasy and high-fiber foods.',
        'if_not_working': 'If diarrhea persists for more than 2 days or causes dehydration, consult a doctor.'
    },
    'constipation': {
        'medications': {
            'fiber supplements': {
                'dosage': 'as per need',
                'link': 'https://www.google.com/search?q=fiber+supplements'
            },
            'laxative': {
                'dosage': 'as directed',
                'link': 'https://www.google.com/search?q=laxative'
            }
        },
        'precautions': 'Increase water intake, exercise regularly.',
        'diet': 'Eat high-fiber foods like fruits, vegetables, and whole grains. Avoid dairy and processed foods.',
        'if_not_working': 'If constipation persists for more than a week or causes severe discomfort, consult a doctor.'
    },
    'hypertension': {
        'medications': {
            'amlodipine': {
                'dosage': '5mg once daily',
                'link': 'https://www.google.com/search?q=amlodipine'
            },
            'losartan': {
                'dosage': '50mg once daily',
                'link': 'https://www.google.com/search?q=losartan'
            }
        },
        'precautions': 'Monitor blood pressure regularly, reduce salt intake, avoid stress.',
        'diet': 'Eat potassium-rich foods (bananas, spinach), avoid salty and fatty foods, limit caffeine.',
        'if_not_working': 'If blood pressure remains uncontrolled, consult a doctor.'
    },
    'diabetes': {
        'medications': {
            'metformin': {
                'dosage': '500mg twice daily',
                'link': 'https://www.google.com/search?q=metformin'
            },
            'insulin': {
                'dosage': 'as prescribed',
                'link': 'https://www.google.com/search?q=insulin'
            }
        },
        'precautions': 'Monitor blood sugar regularly, avoid sugary foods, exercise regularly.',
        'diet': 'Eat a balanced diet with whole grains, lean protein, and vegetables. Avoid processed sugars and carbs.',
        'if_not_working': 'If blood sugar remains uncontrolled, consult a doctor.'
    },
    'asthma': {
        'medications': {
            'inhaler': {
                'dosage': 'as directed',
                'link': 'https://www.google.com/search?q=asthma+inhaler'
            },
            'montelukast': {
                'dosage': '10mg once daily',
                'link': 'https://www.google.com/search?q=montelukast'
            }
        },
        'precautions': 'Avoid allergens, use inhaler before exercise, avoid smoking.',
        'diet': 'Eat anti-inflammatory foods (e.g., ginger, turmeric), avoid processed and fried foods.',
        'if_not_working': 'If asthma attacks become more frequent or severe, consult a doctor.'
    },
    'allergies': {
        'medications': {
            'antihistamine': {
                'dosage': '10mg once daily',
                'link': 'https://www.google.com/search?q=antihistamine'
            }
        },
        'precautions': 'Avoid known allergens, stay indoors during high pollen counts.',
        'diet': 'Eat foods rich in quercetin (e.g., apples, berries), avoid dairy and sugary foods during allergy season.',
        'if_not_working': 'If allergy symptoms worsen or cause trouble breathing, consult a doctor.'
    }
}


        # Medicines that prevent interactions or support overall health
        self.non_reactive_medications = {
            'multivitamin': 'Take once daily to prevent deficiencies.',
            'probiotic': 'Helps maintain gut health, especially with antibiotics.'
        }

    def get_medications(self, conditions):
        meds = {}
        precautions = []
        diet = []
        if_not_working = []

        for condition in conditions:
            if condition in self.conditions:
                condition_info = self.conditions[condition]
                
                # Add medications (ensuring no conflict)
                for med, info in condition_info['medications'].items():
                    if med not in meds:
                        meds[med] = info['dosage']
                        meds[f'{med}_link'] = info['link']  # Store the link separately with a unique key
                
                # Add precautions and diet
                precautions.append(condition_info['precautions'])
                diet.append(condition_info['diet'])
                if_not_working.append(condition_info['if_not_working'])
        
        return meds, precautions, diet , if_not_working

    def suggest_medication(self, conditions):
        medications, precautions, diet , if_not_working = self.get_medications(conditions)
        
        # Preventative non-reactive medications
        prevent_reactions = self.non_reactive_medications

        # Formatting the response
        response = {
            'medications': medications,
            'precautions': precautions,
            'diet': diet,
            'prevent_reactions': prevent_reactions,
            'if_not_working' : if_not_working
        }
        
        return response

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/doctor')
def doctor():
    return render_template('doctor.html')

@app.route('/style')
def style():
    return render_template('styles.css')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/chat', methods=['POST'])
def chat():
    conditions_input = request.form.get('condition').lower()
    conditions = [condition.strip() for condition in conditions_input.split(',')]
    
    chatbot = MedicalChatbot()
    response = chatbot.suggest_medication(conditions)

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=80 ,host='0.0.0.0')