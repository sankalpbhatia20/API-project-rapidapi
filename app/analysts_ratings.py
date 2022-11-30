from openbb_terminal.sdk import openbb
import pandas as pd
import json

def analyst_rating(asset):
    
    df = (openbb.stocks.dd.analyst(asset))

    asset_list = [asset] * len(df)
    try:
        df.reset_index(inplace=True)
        #print(df)

        df['asset'] = asset_list

        result = df.to_json(orient="records")
        analyst_rating_json = json.loads(result)
        
        return analyst_rating_json
        
    except:
        return {"Error" : "Make sure you have entered a valid US stock ticker"}

#analyst_rating(ticker)