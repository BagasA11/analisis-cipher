// import {axios} from '../../node_modules/axios/index'


function generateRandomText(length) {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let result = '';
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        result += characters[randomIndex];
    }
    return result;
}

function removeSpacesAndNumbers(str) {
    return str.replace(/[0-9\s]/g, '');
}

const domLoad = document.addEventListener('DOMContentLoaded', () => {
    let csrfInput = document.getElementById('csrf');
    let csrfText = generateRandomText(64);
    csrfInput.value = csrfText;
})



const submit = document.getElementById("form").addEventListener("submit", function(event) {
    event.preventDefault();
    // retrieve input from content
    const formData = new FormData(event.target);
    const data = {};
    formData.forEach((value, key) => {
    //   console.log(key);
      
      data[key] = value;
    });
    
    // remove space and number char from str
    data['cipher'] = removeSpacesAndNumbers(data['cipher']);
    // create request object
    const url = 'http://127.0.0.1:5000/caesar'
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'Accept':'application/json'
        },
        body: JSON.stringify(data)
    }).then(
        (response) => response.json()
    ).then(
        (data) => {
            const EngLetterFrequency = {
                "a": 8.17,
                "b": 1.49,
                "c": 2.78,
                "d": 4.25,
                "e": 12.70,
                "f": 2.23,
                "g": 2.02,
                "h": 6.09,
                "i": 6.97,
                "j": 0.15,
                "k": 0.77,
                "l": 4.03,
                "m": 2.41,
                "n": 6.75,
                "o": 7.51,
                "p": 1.93,
                "q": 0.10,
                "r": 5.99,
                "s": 6.33,
                "t": 9.06,
                "u": 2.76,
                "v": 0.98,
                "w": 2.36,
                "x": 0.15,
                "y": 1.97,
                "z": 0.07
            };
            
            let plainTextBox = document.getElementById('plain') 
            plainTextBox.value = data['plaintext']
            // console.log(data);
            console.log(data['frequency'])
        }
    );
   
})