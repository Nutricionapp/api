from pydantic import BaseModel
import mercadopago



sdk = mercadopago.SDK("")

class dataMercadoPago (BaseModel):#"no es necesario guardar modelo, solo necesitamos generar el id para usarlo en el frontend"
    title:str
    quantity:int 
    price:float
    timeStampExpiration:str


def getPreferenceID(Mercadopago:dataMercadoPago):#puse get como nombre pero tiene que usarse un metodo post que reciba la data que esta arriba y que responda el id de abajo
    # Crea un elemento en la preferencia
    preference_data = {
    # el "purpose": "wallet_purchase", solo permite pagos registrados
    # para permitir pagos de invitados, puede omitir esta propiedad
        "purpose": "wallet_purchase",
        "items": [
            {
                "title": Mercadopago.title,
                "quantity": Mercadopago.quantity,
                "unit_price": Mercadopago.price
            }
        ],
        "date_of_expiration": Mercadopago.timeStampExpiration,
        "back_urls": {
            "success": "https://nutricion-app-frontend.vercel.app/",
            "failure": "https://nutricion-app-frontend.vercel.app/",
        },
        "auto_return": "approved"
    }
    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]

    return {"preferenceId":preference}

