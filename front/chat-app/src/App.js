import React, { useState } from 'react';
import { addResponseMessage, Widget } from 'react-chat-widget';
import 'react-chat-widget/lib/styles.css';

const App = () => {
    // Hook pour gérer l'historique des messages
    const [chatHistory, setChatHistory] = useState([]);

    // Fonction appelée à chaque nouveau message utilisateur
    const handleNewUserMessage = async (message) => {
        // Mise à jour locale de l'historique des messages
        const updatedHistory = [...chatHistory, { role: "user", content: message }];

        try {
            // Envoi de l'historique au backend
            const response = await fetch("http://127.0.0.1:8000/chat/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ messages: updatedHistory }),
            });

            // Vérification si la requête a réussi
            if (!response.ok) throw new Error("Invalid chat history");

            // Réponse du backend
            const data = await response.json();
            setChatHistory([...updatedHistory, { role: "agent", content: data.reply }]);
            addResponseMessage(data.reply);
        } catch (error) {
            console.error("Error:", error.message);
        }
    };

    // Affichage du composant React-Chat-Widget
    return (
        <div>
          
            <Widget handleNewUserMessage={handleNewUserMessage} 
            title="Chatbot"
            subtitle="Welcome to the chatbot"
            
            />
        </div>
    );
};

export default App;
