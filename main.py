import openai
import config
import typer
from rich import print
from rich.table import Table

#Función para mejorar la visualización de la información en la terminal usando el módulo typer
def main():
    
    #Asigna la api_key que se obtuvo de la página web de OpenAI
    openai.api_key=config.api_key
    
    #Crea un título en negritas y de color verde en la terminal gracias al módulo rich
    print("[bold green]ChatGPT API en Python[/bold green]")
    
    #Crea un tabla en la terminal gracias al módulo rich
    table=Table("Comando","Descripción") 
    table.add_row("exit","Salir de la Aplicación")
    table.add_row("new","Crear una nueva conversación")
    print(table)
    
    #Da contexto al asistente, ejemplo: Eres un programador, eres un traductor, etc.
    context={"role":"system","content":"Eres un asistente muy útil"}
    messages=[context]
    
    #Creamos un ciclo para que el programa siga preguntando y se detenga al escribir exit en la terminal
    while True:
        
        #Asigna nuestra consulta a la variable content (contenido)
        content= __prompt()
       
        if content=="new":
            print("Nueva conversación creada")
            messages=[context]
            content=__prompt()
        
        #Prepara el mensaje que se consultará en chat gpt
        messages.append({"role":"user","content":content})
        
        #Se obtiene la respuesta desde chat gpt y se almacena en la variable response (respuesta)
        response=openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
        
        #Se selecciona sólo la información de utilidad y se guarda como response_content
        response_content=response.choices[0].message.content
        
        #Al mensaje se le modifica el role a assistant para mantener el contexto
        messages.append({"role":"assistant","content":response_content})
        
        #Imprime la respuesta de chatgpt útil y con el contexto anterior
        print(f"[bold green]> [/bold green][green]{response_content}[green]")

def __prompt() -> str:
    prompt=typer.prompt("\n¿Sobre qué quieres hablar?")
    
    if prompt=="exit":
            exit=typer.confirm("!¿Estás Seguro?")
            if exit:
                print("Hasta luego!")
                raise typer.Abort()
            return __prompt()
    return prompt
        
if __name__=="__main__":
    typer.run(main)