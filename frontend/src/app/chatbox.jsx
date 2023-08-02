"use client";

import React, { useEffect, useState, useRef } from 'react';
import { io } from "socket.io-client";
import SplashPage from './splashpage'
import Image from 'next/image';

const socket = io('http://localhost:5000/test');
const initialList = [{ role: "assistant", content: "Hi, is there anything I can help you with?" }];

const ChatBox = ({ inputValue }) => {
    const messagesEndRef = useRef(null);
    const [list, setList] = useState(initialList);

    useEffect(() => {
        if (inputValue != '') {
            const updatedList = [...list, { role: "user", content: inputValue }];

            let socketjson = updatedList.map(({ products, ...item }) => item)
            socket.emit('my_event', socketjson);
            console.log("emmitting " + JSON.stringify(socketjson));

            setList(updatedList);
        }
    }, [inputValue]);

    socket.on("my_response", (msg) => {
        console.log(msg)
        const updatedList = [...list, { role: "assistant", content: msg.data, products: msg.products }];
        setList(updatedList);
    });
    useEffect(() => {
        if (messagesEndRef.current) {
            messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
        }
    }, [list]); // Scroll to bottom whenever list changes
    return (
        <div className="flex justify-items-center text-white">
            <div className="flex flex-col w-screen space-y-4 p-3 overflow-y-auto scrollbar-thumb-blue scrollbar-thumb-rounded scrollbar-track-blue-lighter scrollbar-w-2 scrolling-touch">
                <SplashPage />
                {list.map((item, index) => (
                    item.role == 'assistant' ?
                        <div className="chat-message" key={index}>
                            <div className="flex items-end">
                                <div className="flex flex-col space-y-2 text-xs max-w-xs mx-2 order-2 items-start">
                                    <div>
                                        <span className="px-4 py-2 rounded-lg inline-block rounded-bl-none bg-gray-300 text-gray-600">
                                            {item.content}
                                        </span>
                                    </div>
                                    {item.products && item.products.map((product, productIndex) => (
                                        <div key={productIndex}>
                                            <span className="max-w-xs auto-cols-max px-4 py-2 rounded-lg flex rounded-bl-none bg-gray-300 text-gray-600">

                                                <Image
                                                    src={product.image}
                                                    className="h-20 w-20"
                                                />
                                                <div className='w-full px-4'>
                                                    <div className='text-m font-bold justify-center w-full'>
                                                        {product.name}
                                                    </div>
                                                    <div  className='text-s justify-center max-w-xs'>
                                                        {product.price}
                                                    </div>
                                                    <a href={product.link}>
                                                        <button
                                                            className='text-white bg-black px-2 py-2'
                                                        >
                                                            Learn More
                                                        </button>
                                                    </a>
                                                </div>
                                            </span>
                                        </div>
                                    ))}
                                </div>
                                <Image
                                    src="https://images.unsplash.com/photo-1549078642-b2ba4bda0cdb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=3&w=144&h=144"
                                    alt="My profile"
                                    className="w-6 h-6 rounded-full order-1"
                                />
                            </div>
                        </div>
                        :
                        <div className="chat-message" key={index}>
                            <div className="flex items-end justify-end">
                                <div className="flex flex-col space-y-2 text-xs max-w-xs mx-2 order-1 items-end">
                                    <div>
                                        <span className="px-4 py-2 rounded-lg inline-block rounded-br-none bg-green-900 text-white">
                                            {item.content}
                                        </span>
                                    </div>
                                </div>
                                <Image
                                    src="https://images.unsplash.com/photo-1590031905470-a1a1feacbb0b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=3&w=144&h=144"
                                    alt="My profile"
                                    className="w-6 h-6 rounded-full order-2"
                                />
                            </div>
                        </div>
                ))}
                <div ref={messagesEndRef}></div>
            </div>
        </div>
    );
}


export default ChatBox;