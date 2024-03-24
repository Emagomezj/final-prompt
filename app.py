import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

################ Función para obtener el contexto histórico de un evento histórico específico mediante la API de OpenAI ################
API_KEY = os.getenv("API_KEY")

client = OpenAI(
     api_key = API_KEY
     )
def contexto_historico(evento):
    prompt = f"""
        Contextualiza brevemente un evento histórico especifico, destacando sus aspectos políticos, económicos, culturales y sociales. Utiliza listas para mayor claridad. Evento Histórico: {evento}'

        **1. Aspectos Políticos: **

        - [Breve descripción del contexto político]
        - [Influencia de líderes o figuras políticas]
        
        **2. Aspectos Económicos:**

        - [Impacto en la economía y recursos]
        - [Cambios en políticas económicas]
        
        **3. Aspectos Culturales:**

        - [Acontecimientos culturales relevantes]
        - [Influencia en la expresión artística y cultural]
        
        **4. Aspectos Sociales:**

        - [Efectos en la sociedad y la vida cotidiana]
        - [Cambios en la estructura social] """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "user",
            "content": prompt
            }
        ]
    )
    contexto = response.choices[0].message.content
    print(contexto)
    
    return contexto


######## Definición de la función principal para la aplicación web ########

def main ():
    #Título
    st.title("Cronoscopio")
    
    #Descripción
    
    description = 'Cronoscopio es una aplicación web que le brindará puntos claves para comprender el contexto en el que se desarrolla un evento histórico, se basará en el aspecto Social, Político, Cultural y Económico del mismo.'
    
    st.write(description)
    
    #Instrucciones
    
    st.text('Para utilizarla solo deberá:')
    st.text('1- Ingresar el evento histórico que le interesa en el recuadro destinado a tal fin.')
    st.text('2- Presionar el botón "Obtener contexto" para obtener el cronoscopio de ese evento.')
    st.text('3- Puede descargar la respuesta en un archivo ".txt" oprimiendo descargar.')
    
    #Input del evento histórico
    evento = st.text_input("Ingrese el evento histórico: ")

    #Botón respuesta
    if st.button("Obtener contexto"):
        if evento != "":
            respuesta = contexto_historico(evento)
            st.write(respuesta)
            st.download_button(
                label="Descargar",
                data= respuesta,
                file_name=f"cronoscopio - {evento}.txt ",
                mime="text/markdown"
            )
        else:
            st.write("Por favor ingrese un evento histórico.")

######## Llamada a la función principal ########



if __name__ == "__main__":
    main()
    

    
