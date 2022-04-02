for record in event ['records']:
    #Decode the incoming data and convert it to a list
    payLoad_dec = base64.b64decode(record['data']).decode().split(" ")
    # Multiply the speed Component by 1.60934 to convert to kph
    payLoad_dec[5] = str(float(payLoad_dec[5]) * 1.60934)
    # Re-Encode the payload
    payLoad = " ".join(payLoad_dec)
    payLoad_enc = base64.b64encode(payLoad.encode())
    # Prepare the record
    output.append({
        'recordId': record['recordId'],
        'result': 'ok',
        'data': payLoad_enc,
    })
    #Return all the records!
    print ({'records': output})