import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring
import random
import string
from xml.dom import minidom


def generate_random_element(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def title_doc(root, xml_path):
    titre = ET.Element("Titre")
    element_a_enlever = ["base de connaissance\daitement\Fichier TRIER", '.xml']
    for element in element_a_enlever:
        xml_path = xml_path.replace(element, "").strip()
    titre.text = xml_path
    root.insert(0, titre)


def balise_docid(root):
    # Obtenir l'élément racine de l'arbre XML    
    # Création de la balise <docid>
    docid_element = ET.Element("docid")

    # Ajout d'un seul élément aléatoire à la balise <docid> avec une longueur de 10 caractères
    random_element = generate_random_element()
    docid_element.text = str(random_element)

    # Insérer docid_element comme le premier enfant de root
    root.insert(1, docid_element)

    print('BABABABABA')


    



def analyser_texte(texte):
    resultat = []
    en_attente = False
    phrase_en_cours = ""

    mots_cles = ['Solution', 'Détails', 'Remarques', 'Cause', 'NEWPORTTEXT', 'Procédure']

    lignes = texte.split('\n')

    for ligne in lignes:
        if 'Erreur' in ligne:
            en_attente = True
            phrase_en_cours = '' + ligne
        elif en_attente:
            phrase_en_cours += '\n' + ligne
            for mot_cle in mots_cles:
                if mot_cle in ligne:
                    # Supprimer le mot-clé de la phrase
                    phrase_en_cours = phrase_en_cours.split(mot_cle)[0]
                    resultat.append(phrase_en_cours)
                    en_attente = False
                    break

    return resultat

def analyser_texte_two(texte):
    resultat = []
    en_attente = False
    phrase_en_cours = ""

    mots_cles = ['Solution', 'Détails', 'Remarques', 'Erreur', 'NEWPORTTEXT']

    lignes = texte.split('\n')

    for ligne in lignes:
        if 'Cause' in ligne:
            en_attente = True
            phrase_en_cours = '' + ligne
        elif en_attente:
            phrase_en_cours += '\n' + ligne
            for mot_cle in mots_cles:
                if mot_cle in ligne:
                    # Supprimer le mot-clé de la phrase
                    phrase_en_cours = phrase_en_cours.split(mot_cle)[0]
                    resultat.append(phrase_en_cours)
                    en_attente = False
                    break

    return resultat

def analyser_texte_three(texte):
    resultat = []
    en_attente = False
    phrase_en_cours = ""

    mots_cles = ['Détails', 'Remarques', 'NEWPORTTEXT']

    lignes = texte.split('\n')

    for ligne in lignes:
        if 'Solution' in ligne:
            en_attente = True
            phrase_en_cours = '' + ligne
        elif en_attente:
            phrase_en_cours += '\n' + ligne
            for mot_cle in mots_cles:
                if mot_cle in ligne:
                    # Supprimer le mot-clé de la phrase
                    phrase_en_cours = phrase_en_cours.split(mot_cle)[0]
                    resultat.append(phrase_en_cours)
                    en_attente = False
                    break

    return resultat

def analyser_texte_four(texte):
    resultat = []
    en_attente = False
    phrase_en_cours = ""

    mots_cles = ['Solution', 'Cause', 'Erreur', 'Remarques', 'NEWPORTTEXT']

    lignes = texte.split('\n')

    for ligne in lignes:
        if 'Détails' in ligne:
            en_attente = True
            phrase_en_cours = '' + ligne
        elif en_attente:
            phrase_en_cours += '\n' + ligne
            for mot_cle in mots_cles:
                if mot_cle in ligne:
                    # Supprimer le mot-clé de la phrase
                    phrase_en_cours = phrase_en_cours.split(mot_cle)[0]
                    resultat.append(phrase_en_cours)
                    en_attente = False
                    break

    return resultat


def analyser_texte_five(texte):
    resultat = []
    en_attente = False
    phrase_en_cours = ""

    mots_cles = ['NEWPORTTEXT']

    lignes = texte.split('\n')

    for ligne in lignes:
        if 'Remarques' in ligne:
            en_attente = True
            phrase_en_cours = '' + ligne
        elif en_attente:
            phrase_en_cours += '\n' + ligne
            for mot_cle in mots_cles:
                if mot_cle in ligne:
                    # Supprimer le mot-clé de la phrase
                    resultat.append(phrase_en_cours)
                    en_attente = False
                    break

    return resultat




def erreur_xml(root, text):
    resultat_analyse = analyser_texte(text)
    
    for phrase in resultat_analyse:
        erreur_xml = ET.Element('Erreur')
        erreur_xml.text = phrase
        root.insert(2, erreur_xml)

def cause_xml(root, text):
    resultat_analyse = analyser_texte_two(text)
    
    for phrase in resultat_analyse:
        cause_xml = ET.Element('Cause')
        cause_xml.text = phrase
        root.insert(3, cause_xml)

def solution_xml(root, text):
    resultat_analyse = analyser_texte_three(text)
    
    for phrase in resultat_analyse:
        solution_xml = ET.Element('Solution')
        solution_xml.text = phrase
        root.insert(4, solution_xml)

def details_xml(root, text):
    resultat_analyse = analyser_texte_four(text)
    
    for phrase in resultat_analyse:
        details_xml = ET.Element('Détails')
        details_xml.text = phrase
        root.insert(5, details_xml)


def remarque_xml(root, text):
    resultat_analyse = analyser_texte_five(text)
    
    for phrase in resultat_analyse:
        remarque_xml = ET.Element('Remarques-techniques')
        remarque_xml.text = phrase
        root.insert(6, remarque_xml)
        print('OKKKKKKK')



def contenue_xml(root, text):
    contenue_xml = ET.Element('TEXTE')
    contenue_xml.text = text
    root.insert(7, contenue_xml)

















def analyser_texte_six(texte):
    resultat = []
    en_attente = False
    phrase_en_cours = ""

    mots_cles = ['Procédure', 'Détaillée', 'Remarques', 'NEWPORTTEXT']

    lignes = texte.split('\n')

    for ligne in lignes:
        if "Note d'attention" in ligne:
            en_attente = True
            phrase_en_cours = '' + ligne
        elif en_attente:
            phrase_en_cours += '\n' + ligne
            for mot_cle in mots_cles:
                if mot_cle in ligne:
                    # Supprimer le mot-clé de la phrase
                    phrase_en_cours = phrase_en_cours.split(mot_cle)[0]
                    resultat.append(phrase_en_cours)
                    en_attente = False
                    break
    
    print('resultat', resultat)
    return resultat





def analyser_texte_seven(texte):
    resultat = []

    en_attente = False
    phrase_en_cours = ""

    mots_cles = ['Détaillée', 'Remarques', 'NEWPORTTEXT', 'Procédure']

    lignes = texte.split('\n')

    for ligne in lignes:
        if "Procédure" in ligne:
            en_attente = True
            phrase_en_cours = '' + ligne
        elif en_attente:
            phrase_en_cours += '\n' + ligne
            for mot_cle in mots_cles:
                if mot_cle in ligne:
                    # Supprimer le mot-clé de la phrase
                    phrase_en_cours = phrase_en_cours.split(mot_cle)[0]
                    resultat.append(phrase_en_cours)
                    en_attente = False
                    break
    
    print('resultat 2', resultat)
    return resultat

def analyser_texte_eight(texte):
    resultat = []

    en_attente = False
    phrase_en_cours = ""

    mots_cles = ['Remarques', 'NEWPORTTEXT']

    lignes = texte.split('\n')

    for ligne in lignes:
        if "Détaillé" in ligne:
            en_attente = True
            phrase_en_cours = '' + ligne
        elif en_attente:
            phrase_en_cours += '\n' + ligne
            for mot_cle in mots_cles:
                if mot_cle in ligne:
                    # Supprimer le mot-clé de la phrase
                    phrase_en_cours = phrase_en_cours.split(mot_cle)[0]
                    resultat.append(phrase_en_cours)
                    en_attente = False
                    break
    
    print('resultat 2', resultat)
    return resultat


def analyser_texte_nine(texte):
    resultat = []

    en_attente = False
    phrase_en_cours = ""

    mots_cles = ['NEWPORTTEXT', 'Remarques', 'Détaillée', 'Procédure', 'Cause', 'Erreur', 'Solution', 'Consigne bdf']

    lignes = texte.split('\n')

    for ligne in lignes:
        if "Consignes" in ligne:
            en_attente = True
            phrase_en_cours = '' + ligne
        elif "Consigne" in ligne:
            en_attente = True
            phrase_en_cours = '' + ligne
        elif 'Consigne bdf' in ligne:
            break
        elif en_attente:
            phrase_en_cours += '\n' + ligne
            for mot_cle in mots_cles:
                if mot_cle in ligne:
                    # Supprimer le mot-clé de la phrase
                    phrase_en_cours = phrase_en_cours.split(mot_cle)[0]
                    resultat.append(phrase_en_cours)
                    en_attente = False
                    break
    
    return resultat














def note_xml(root, text):
    resultat_analyse = analyser_texte_six(text)
    
    for phrase in resultat_analyse:
        note_xml = ET.Element('note-dattention')
        note_xml.text = phrase
        root.insert(3, note_xml)
        print('OKKKKKKK')



def procedure_xml(root, text):
    resultat_analyse = analyser_texte_seven(text)
    
    for phrase in resultat_analyse:
        procedure_xml = ET.Element('Procedure')
        procedure_xml.text = phrase
        root.insert(4, procedure_xml)
        print('OKKKKKKK')


def Détaillé_xml(root, text):
    resultat_analyse = analyser_texte_eight(text)
    
    for phrase in resultat_analyse:
        procedure_xml = ET.Element('Procedure-detaillee')
        procedure_xml.text = phrase
        root.insert(5, procedure_xml)
        print('OKKKKKKK')


def texte_xml(root, text):
    procedure_xml = ET.Element('Procedure')
    procedure_xml.text = text
    root.insert(5, procedure_xml)
    print('OKKKKKKK')


def consignes_xml(root, text):
    resultat_analyse = analyser_texte_nine(text)
    
    for phrase in resultat_analyse:
        procedure_xml = ET.Element('Consignes')
        procedure_xml.text = phrase
        root.insert(4, procedure_xml)
        print('OKKKKKKK')


def create_self_closing_tag(root, text):
    # Recherche du début et de la fin de la balise
    start_index = text.find("Image")
    end_index = text.find("png")

    # Vérification si les indices sont valides
    if start_index != -1 and end_index != -1:
        # Créer un nouvel élément
        image_element = ET.Element("image")
        # Insérer le nouvel élément dans l'élément racine
        root.insert(0, image_element)
        return root
    else:
        # Si l'un des mots clés n'est pas trouvé, retourner l'élément racine inchangé
        return root
