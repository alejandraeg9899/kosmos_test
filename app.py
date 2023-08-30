from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)
nlp = spacy.load('es_core_news_sm')


@app.route('/ner', methods=['POST'])
def recognize_entities():
    data = request.get_json()
    sentences = data.get('oraciones', [])

    entities_in_sentences = []
    response = []

    for sentence in sentences:
        doc = nlp(sentence)
        entities_by_sentence = {}
        
        for ent in doc.ents:
            entities_by_sentence[ent.text] = ent.label_

        
        response.append({
            "oración": sentence,
            "entidades": entities_by_sentence
        })
        
    entities_in_sentences.append({
        'resultado': response 
    })

    return jsonify(entities_in_sentences)


def main():
    app.run(debug=True)
    recognize_entities()

if __name__ == '__main__':
    main()