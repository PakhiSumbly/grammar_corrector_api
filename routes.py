from flask import Blueprint, request, jsonify
from grammar_checker import correct_grammar

correct_grammar_route = Blueprint('correct_grammar_route', __name__)

@correct_grammar_route.route('/check_grammar', methods=['POST'])
def check_grammar_route_handler():
    
    sentence = request.json.get('sentence', '')
    
    if not sentence:
        return jsonify({'error': 'No sentence provided'}), 400

    corrected_sentence = correct_grammar(sentence)
    
    return jsonify({
        'original_sentence': sentence,
        'corrected_sentence': corrected_sentence
    })
