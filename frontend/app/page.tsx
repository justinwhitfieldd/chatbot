"use client";

import Image from 'next/image'
import React, { useState } from 'react';
import { useRef, useEffect } from "react";
import axios from 'axios';

// List data example
const initialList = [{ image: '', messages: [], response: "Hi, is there anything I can help you with?" }];



export default function Home() {

  const [list, setList] = useState(initialList);
  const [inputValue, setInputValue] = useState('');

  const ListPage = () => {
    return (
      <div>
        {list.map((item, index) => (
          <div className="msg-btn-holder">
            <div className={index % 2 == 1 ? "sender-msg msg-btn" : "receiver-msg msg-btn"}>
              <p>{item.response}</p>
            </div>
            {item.image != '' &&
              <img src={item.image} width="50" height="50"></img>
              }
          </div>
        ))}
      </div>
    )
  };

  const handleAddItem = async () => {
    if (inputValue.trim() !== '' && list.length % 2 === 1) {
      const updatedList = [...list, { image: '', messages: [], response: inputValue }];
      const params = updatedList.map((item) => `message=${encodeURIComponent(item.response)}`).join('&');
      const apiUrl = `http://127.0.0.1:5000/balls?${params}`;
  
      try {
        const response = await axios.get(apiUrl);
        const { image, messages, response: apiResponse } = response.data;
  
        const updatedItem = { image, messages, response: apiResponse };
        updatedList.push(updatedItem);
  
        setList(updatedList);
        setInputValue('');
        console.log('Updated List:', list);
        console.log('API Response:', apiResponse);
      } catch (error) {
        console.error('API Error:', error);
      }
    }
  };

  const contentRef = useRef(null);
  useEffect(() => {
    // Scroll to the bottom of the content
    contentRef.current.scrollTop = contentRef.current.scrollHeight;
  }, [ListPage]); // Update the scroll position whenever ListPage updates
  

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <>
        <meta charSet="UTF-8" />
        <title>CodePen - Enchanted Forest Chat</title>
        <link rel="stylesheet" href="./style.css" />
        {/* partial:index.partial.html */}
        <link
          rel="stylesheet"
          href="https://site-assets.fontawesome.com/releases/v6.2.1/css/all.css"
          crossOrigin="anonymous"
          referrerPolicy="no-referrer"
        />
        <img
          id="backgroundimg"
          src="https://images.pexels.com/photos/418831/pexels-photo-418831.jpeg?cs=srgb&dl=pexels-rudolf-jakkel-418831.jpg&fm=jpg"
        />
        <div className="main">
          <div className="header">
            <i
              style={{ cursor: "pointer", display: "flex", float: "right" }}
              className="fas fa-arrow-left"
            />
            <div className="notifications">
              <b>3</b>
            </div>
            <div className="center">
              <div>
                <img
                  src="https://i.pinimg.com/originals/4e/f2/66/4ef266b2e215a6b61bfb0259b11f1891.png"
                  width={50}
                  height={50}
                />
              </div>
            </div>
          </div>
          <div className="content" ref={contentRef}>
            <div style={{ padding: 11 }}>
              <p>Thur, May 26, 10:41 AM</p>
              <ListPage></ListPage>
            </div>
          </div>
          <div className="footer">
            <div style={{ width: "100%", padding: 11 }}>
              <input
                type="text"
                placeholder="Message"
                className="text-box"
                name="message"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === "Enter") {
                    handleAddItem();
                  }
                }}
              />
              <div className="send-ico" onClick={handleAddItem}>
                <button
                  style={{ position: "absolute" }}
                  onClick={handleAddItem}
                  className="fas fa-paper-plane"
                />
              </div>
            </div>
          </div>
        </div>
        {/* partial */}
      </>
    </main>
  )
}
 