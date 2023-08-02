import React from 'react';

const SplashPage = () => {
    return (
        <>
            <div className="md:hidden w-3/4 justify-stretch self-center">
                <div className="basis-1/3">
                    <h1 className="w-full text-white text-center text-xl">CAPABILITIES</h1>
                    <div className="bg-black bg-opacity-75 rounded-xl text-white text-center hover:bg-opacity-90 py-2">
                        Remembers what user said earlier in the conversation
                        <br />
                        <br />
                        Allows user to provide follow-up corrections
                        <br />
                        <br />
                        Trained to decline inappropriate requests
                    </div>
                </div>
                <div className="basis-1/3 items-center">
                    <h1 className="w-full text-white text-center text-xl">
                        ASK ME ANYTHING
                    </h1>
                    <div className="flex-col space-y-3 px-1 self-center">
                        <div className="bg-black bg-opacity-75 rounded-xl text-white text-center py-2">
                            “What are the benefits of using natural skincare products?”
                        </div>
                        <div className="bg-black bg-opacity-75 rounded-xl text-white text-center py-2">
                            “Are your products suitable for sensitive skin”
                        </div>
                        <div className="bg-black bg-opacity-75 rounded-xl text-white text-center py-2">
                            “Do you offer any products for anti-aging?”
                        </div>
                        <div className="bg-black bg-opacity-75 rounded-xl text-white text-center py-2">
                            “Can you provide information about your sustainability practices?”
                        </div>
                    </div>
                </div>
                <div className="basis-1/3">
                    <h1 className="w-full text-white text-center text-xl">DISCLAIMERS</h1>
                    <div className="bg-black bg-opacity-75 rounded-xl text-white text-center">
                        May occasionally generate incorrect information
                        <br />
                        <br />
                        May occasionally produce harmful instructions or biased content
                        <br />
                        <br />
                        Limited knowledge after 2021
                    </div>
                </div>
            </div>
            <div className="hidden md:flex md:flex-row w-3/4 justify-stretch self-center">
                <div className="basis-1/3">
                    <h1 className="w-full text-white text-center text-xl">CAPABILITIES</h1>
                    <div className="bg-black bg-opacity-75 rounded-xl text-white text-center hover:bg-opacity-90 py-2">
                        Remembers what user said earlier in the conversation
                        <br />
                        <br />
                        Allows user to provide follow-up corrections
                        <br />
                        <br />
                        Trained to decline inappropriate requests
                    </div>
                </div>
                <div className="basis-1/3 items-center">
                    <h1 className="w-full text-white text-center text-xl">
                        ASK ME ANYTHING
                    </h1>
                    <div className="flex-col space-y-3 px-1 self-center">
                        <div className="bg-black bg-opacity-75 rounded-xl text-white text-center py-2">
                            “What are the benefits of using natural skincare products?”
                        </div>
                        <div className="bg-black bg-opacity-75 rounded-xl text-white text-center py-2">
                            “Are your products suitable for sensitive skin”
                        </div>
                        <div className="bg-black bg-opacity-75 rounded-xl text-white text-center py-2">
                            “Do you offer any products for anti-aging?”
                        </div>
                        <div className="bg-black bg-opacity-75 rounded-xl text-white text-center py-2">
                            “Can you provide information about your sustainability practices?”
                        </div>
                    </div>
                </div>
                <div className="basis-1/3">
                    <h1 className="w-full text-white text-center text-xl">DISCLAIMERS</h1>
                    <div className="bg-black bg-opacity-75 rounded-xl text-white text-center">
                        May occasionally generate incorrect information
                        <br />
                        <br />
                        May occasionally produce harmful instructions or biased content
                        <br />
                        <br />
                        Limited knowledge after 2021
                    </div>
                </div>
            </div>
        </>
    );
}

export default SplashPage;