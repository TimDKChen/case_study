
const apiFetch = (method, path, token, body) => {
  const options = {
    method: method,
    headers: { 
      'Content-Type': 'application/json',
      'Accept': 'application/json' 
    },
    body: (method && (method.toUpperCase() === 'POST' || method.toUpperCase() === 'PUT')) ? JSON.stringify(body || {}) : undefined,
  };
  if (token !== null) {
    options.headers.Authorization = `Bearer ${token}`;
  }
  // const url = `http://3.26.232.176:8000/${path}`;
  const url = `http://localhost:5000/${path}`;
  return new Promise((resolve, reject) => {
    fetch(url, options)
      .then((res) => {
        if (res.status === 400 || res.status === 404) {
          res.json().then((errorMsg) => {
            reject(errorMsg.error);
          });
        } else if (res.status === 200) {
          res.json().then(data => {
            resolve(data);
          });
        }
      });
  });
};

export default apiFetch;
