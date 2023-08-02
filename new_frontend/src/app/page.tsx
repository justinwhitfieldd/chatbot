"use client";

import React, { useState } from 'react';
import ChatBox from './chatbox'


export default function Home() {

  const [currentText, setCurrentText] = useState('');
  const [userInput, setUserInput] = useState('');

  const handleMessage = () =>
  {
    setUserInput(currentText);
    console.log("handling message " + userInput);
    setCurrentText('');
  }

  return (
    <>
      <meta charSet="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>ORIGINS AI</title>
      <link
        href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css"
        rel="stylesheet"
      />
      {/* <nav class="flex justify-center items-center bg-white py-4 px-6">
			<div>
				<a href="/" class="text-black font-extralight text-2xl">ORIGINS AI</a>
			</div>
		</nav> */}

      <div className="h-screen w-full flex flex-col bg-cover -z-20 bg-[url('/backgroundtrees.png')]">
        <div className="flex-none">
          <br />
          <br />
          <p className="lg:text-6xl flex justify-center text-white text-xl">
            ORIGINS ASSISTANT
          </p>
          <p className="lg:text-xl text-sm flex justify-center text-white">
            Powered by Artificial Intelligence Technology
          </p>
        </div>
        <div className="flex-grow overflow-y-auto">
          <ChatBox inputValue={userInput} />
        </div>
        <div className="w-full py-3 px-5 h-20 flex-none inline-flex">
          <input
            className="w-full bg-gray-300 px-3 rounded-l-xl bottom-0"
            type="text"
            placeholder="type your message here..."
            onChange = {(e) => setCurrentText(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                handleMessage();
              }
            }}
          />
          <button className="bg-green-900 hover:bg-green-900 text-gray-800 font-bold py-2 px-4 rounded-r-xl inline-flex items-center"
            onClick={handleMessage}>
            <span className="text-white">Send</span>
          </button>
        </div>
      </div>
    </>

  )
}
