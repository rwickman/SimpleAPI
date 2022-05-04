//const APIEndpoint = "http://10.101.200.69:5000/request_file";
const APIEndpoint = "http://0.0.0.0:5000/request_file";

const fakeRequest = {
    "user_id": 1,
    "file_id": 0
};

const requestFile = async () => {
    const response = await fetch(APIEndpoint, {
      method: "POST",
      body: JSON.stringify(fakeRequest),
      headers: {
        'Accept': 'application/json, text/plain, */*',
        'Content-type': 'application/json'
      }
    });
    console.log(response);
    const myJson = await response.json(); //extract JSON from the http response
    console.log(myJson);
};
  

const pingRequestStatus = async () => {
    const response = await fetch(APIEndpoint, {
      method: "GET",
      body: JSON.stringify(fakeRequest),
      headers: {
        'Accept': 'application/json, text/plain, */*',
        'Content-type': 'application/json'
      }
    });
    console.log(response);
    const myJson = await response.json(); //extract JSON from the http response
    console.log(myJson);
    // do something with myJson
};