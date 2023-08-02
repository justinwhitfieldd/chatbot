"use client";

import Image from 'next/image'
import React, { useState, useEffect, useRef } from 'react';
import { io } from "socket.io-client";
import axios from 'axios';

const socket = io('http://localhost:5000/test');

// List data example
const initialList = [{ role: "user", product: { link: '', image: '', name: '', price: '' }, messages: [], response: "Hi, is there anything I can help you with?" }];



export default function Home() {

  const [list, setList] = useState(initialList);
  const [inputValue, setInputValue] = useState('');

 const ListPage = () => {
    return (
      <div>
        {list.map((item, index) => (
    <div className="msg-btn-holder">
        <div className={item.role === "assistant" ? "sender-msg msg-btn" : "receiver-msg msg-btn"}>
            <p>{item.response}</p>
        </div>
        {Array.isArray(item.product) &&
            <div className="product-container">
                {item.product.map(productItem => (
                    productItem.link !== '' &&
                    <div className="relative m-5 w-32 max-w-xs flex flex-col overflow-hidden rounded-lg border border-gray-100 bg-white shadow-md">
                        <div className="h-32 w-full overflow-hidden">
                            <img src={productItem.image} className="object-cover h-full w-full" />
                        </div>
                        <div className="px-4 py-2">
                            <h2 className="font-bold text-xs mb-1">{productItem.name}</h2>
                            <p className="text-gray-700 text-sm">{productItem.price}</p>
                            <a href={productItem.link} className="text-blue-500 hover:text-blue-800 underline mt-2 inline-block">Link</a>
                        </div>
                    </div>
                ))}
            </div>
        }
    </div>
))}




      </div>
    )
  };

  const handleAddItem = async () => {
    // if (inputValue.trim() !== '' && list.length % 2 === 1) {
    //   socket.emit('my_event', { data: inputValue });
    //   setInputValue('');
    // }
    socket.emit('my_event', {data: inputValue});
  };

  const contentRef = useRef(null);
  useEffect(() => {
    socket.on("my_response", (msg) => {
      console.log(msg)
      //const updatedList = [...list, { response: msg.data, product: msg.product_data }];
      //setList(updatedList);
    });
  
    // Cleanup on unmount
    return () => {
      socket.off("my_response");
    };
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
                  // onClick={handleAddItem}
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
