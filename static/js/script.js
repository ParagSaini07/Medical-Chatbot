document.addEventListener('DOMContentLoaded', function () {
    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('nav a');

    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                e.preventDefault();  // Prevent only for internal links
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Add a class to the header when scrolling
    const header = document.querySelector('header');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // Chatbot modal functionality
    const chatbotButton = document.querySelector('.learn-more');
    const modal = document.getElementById('chatbot-modal');
    const closeButton = document.querySelector('.close-button');

    chatbotButton.addEventListener('click', function () {
        modal.style.display = 'block';  // Show the modal
    });

    closeButton.addEventListener('click', function () {
        modal.style.display = 'none';  // Hide the modal
    });

    window.addEventListener('click', function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';  // Hide the modal if clicking outside
        }
    });
});

// Function to redirect to the medication purchase link
function redirect(link) {
    window.open(link, '_blank');
}

// Function to handle sending the message to the backend and displaying the response
function sendMessage() {
    const condition = document.getElementById('condition').value;

    if (condition === '') {
        alert('Please enter your medical condition(s).');
        return;
    }

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `condition=${encodeURIComponent(condition)}`
    })
    .then(response => response.json())
    .then(async (data) => { // Mark as async to use translation API
        const responseDiv = document.getElementById('response');
        responseDiv.style.display = 'block';

        if (data.error) {
            responseDiv.innerHTML = `<p>${data.error}</p>`;
        } else {
            // Display medications
            let medsHtml = '<h3>Medications:</h3><ul>';
            let medsText = 'Medications include: '; // Plain text for speech synthesis
            for (const [med, value] of Object.entries(data.medications)) {
                if (!med.includes('_link')) {
                    const dose = value;
                    const link = data.medications[`${med}_link`] || '#';
                    medsHtml += `
                        <li>
                            ${med}: ${dose}
                            <button class="link_btn" onclick="redirect('${link}')">Buy ${med}</button>
                        </li>`;
                    medsText += `${med}, ${dose}. `; // Add to the text to speak
                }
            }
            medsHtml += '</ul>';

            // Display precautions
            let precautionsHtml = '<h3>Precautions:</h3><ul>';
            let precautionsText = 'Precautions include: '; // Plain text for speech synthesis
            data.precautions.forEach(precaution => {
                precautionsHtml += `<li>${precaution}</li>`;
                precautionsText += `${precaution}. `;
            });
            precautionsHtml += '</ul>';

            // Display diet recommendations
            let dietHtml = '<h3>Diet Recommendations:</h3><ul>';
            let dietText = 'Diet recommendations include: '; // Plain text for speech synthesis
            data.diet.forEach(dietItem => {
                dietHtml += `<li>${dietItem}</li>`;
                dietText += `${dietItem}. `;
            });
            dietHtml += '</ul>';

            // Display preventative medications
            let preventHtml = '<h3>Preventative Medications:</h3><ul>';
            let preventText = 'Preventative medications include: '; // Plain text for speech synthesis
            for (const [med, suggestion] of Object.entries(data.prevent_reactions)) {
                preventHtml += `<li>${med}: ${suggestion}</li>`;
                preventText += `${med}, ${suggestion}. `;
            }
            preventHtml += '</ul>';

            // Display IMPORTANT recommendations
            let impHtml = '<h3 style="color: red;">IMPORTANT:</h3><ul>';
            let impText = 'Important notes: '; // Plain text for speech synthesis
            data.if_not_working.forEach(impItem => {
                impHtml += `<li>${impItem}</li>`;
                impText += `${impItem}. `;
            });
            impHtml += '</ul>';

            responseDiv.innerHTML = medsHtml + precautionsHtml + dietHtml + preventHtml + impHtml;

            // Combine all sections into a single text string for speech
            let speechText = `${medsText} ${precautionsText} ${dietText} ${impText}`;

            // Call the translation function before using speech synthesis
            const translatedText1 = await translateToHindi(`${medsText}`);
            const translatedText2 = await translateToHindi(`${precautionsText}`);
            const translatedText3 = await translateToHindi(`${dietText}`);
           // const translatedText4 = await translateToHindi(`${preventText}`);
            const translatedText5 = await translateToHindi(`${impText}`);
            // Check if the browser supports speech synthesis
            if ('speechSynthesis' in window) {
                // Use Web Speech API to speak the dynamically generated text in Hindi
                const synth = window.speechSynthesis;
                const utterThis1 = new SpeechSynthesisUtterance(translatedText1);
                const utterThis2 = new SpeechSynthesisUtterance(translatedText2);
                const utterThis3 = new SpeechSynthesisUtterance(translatedText3);
               // const utterThis4 = new SpeechSynthesisUtterance(translatedText4);
                const utterThis5 = new SpeechSynthesisUtterance(translatedText5);
                utterThis1.lang = 'hi-IN'; // Set language to Hindi
                utterThis2.lang = 'hi-IN';
                utterThis3.lang = 'hi-IN';
                //utterThis4.lang = 'hi-IN';
                utterThis5.lang = 'hi-IN';

                // Optional: Set the voice to a specific one, if available
                const voices = synth.getVoices();
                const selectedVoice = voices.find(voice => voice.lang === 'en-US');
                if (selectedVoice) {
                    utterThis.voice = selectedVoice;
                }

                // Speak the translated Hindi text
                synth.speak(utterThis1);
                synth.speak(utterThis2);
                synth.speak(utterThis3);
               // synth.speak(utterThis4);
                synth.speak(utterThis5);
            } else {
                console.error('Speech Synthesis API is not supported in this browser.');
            }
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Function to handle speech recognition and convert voice input into text
function startListening() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    recognition.start();

    recognition.onresult = function (event) {
        let transcript = event.results[0][0].transcript;

        // Replace the word "and" with a comma
        transcript = transcript.replace(/\band\b/g, ',');

        // Insert the transformed transcript into the text input
        document.getElementById('condition').value = transcript;
    };

    recognition.onerror = function (event) {
        console.error('Speech recognition error detected: ' + event.error);
    };
}

// Function to translate text to Hindi using LibreTranslate API
async function translateToHindi(text) {
    
    const res = await fetch("http://localhost:5000/translate", {
        method: "POST",
        body: JSON.stringify({
            q: text,
            source: "auto",
            target: "hi",
            format: "text",
            alternatives: 3,
            api_key: "" // If you have an API key, add it here.
        }),
        headers: { "Content-Type": "application/json" }
    });

    const responseData = await res.json();
    return responseData.translatedText; // Get the translated Hindi text
}