# Currency-Converter-Microservice

Requesting/Receiving Data:

Requests can be made using ZeroMQ on local port tcp://localhost:5555. You are free to change this port if needed. A string object will need to be encoded and sent to the currency converter microservice. This object will need to include the monetary value, old currency code, and new currency code in that order. These values will need to have a space between each other within the string object. 

Please see example request below:
<img width="919" alt="Screenshot 2024-05-20 at 9 12 45 PM" src="https://github.com/keonu94/Currency_Converter_Microservice/assets/91299772/cdf4fe08-5eb0-4df5-b36d-0c6c6f545dab">

The microservice will then take the object and decode it. Once decoded, it will calculate the new currency value and send an encoded string object back. 

Please see example response below:
<img width="874" alt="Screenshot 2024-05-20 at 9 16 50 PM" src="https://github.com/keonu94/Currency_Converter_Microservice/assets/91299772/e15dc02f-c2eb-4583-912e-ae941e4c5fdb">

The string object will need to be decoded. This object will include the old monetary value/currency code and new monetary value/currency code (Example: 20.0 USD is equal to 18.42 EUR). 

Please see example of how to receive reply:
<img width="915" alt="Screenshot 2024-05-20 at 9 13 27 PM" src="https://github.com/keonu94/Currency_Converter_Microservice/assets/91299772/6afb9280-2085-460b-8438-7bf068ede6ea">



UML Diagram:
<img width="1126" alt="Screenshot 2024-05-20 at 9 19 56 PM" src="https://github.com/keonu94/Currency_Converter_Microservice/assets/91299772/6025620d-83ed-4f05-8cf3-02e725ca9c2a">
