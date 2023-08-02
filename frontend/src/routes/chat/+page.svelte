<script>
	import ChatBox from './ChatBox.svelte';
	import SplashPage from './SplashPage.svelte';
</script>

<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>ORIGINS AI</title>
		<link
			href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css"
			rel="stylesheet"
		/>
	</head>
	<body class="bg-black">
		<!-- <nav class="flex justify-center items-center bg-white py-4 px-6">
			<div>
				<a href="/" class="text-black font-extralight text-2xl">ORIGINS AI</a>
			</div>
		</nav> -->

		<div
			class="flex flex-col w-screen space-y-4 p-3 overflow-y-auto scrollbar-thumb-blue scrollbar-thumb-rounded scrollbar-track-blue-lighter scrollbar-w-2 scrolling-touch"
		>
			<div class="md:hidden w-3/4 justify-stretch self-center">
				<div class="basis-1/3">
					<h1 class="w-full text-white text-center text-xl">CAPABILITIES</h1>
					<div
						class="bg-black bg-opacity-75 rounded-xl text-white text-center hover:bg-opacity-90 py-2"
					>
						Remembers what user said earlier in the conversation
						<br />
						<br />
						Allows user to provide follow-up corrections
						<br />
						<br />
						Trained to decline inappropriate requests
					</div>
				</div>
				<div class="basis-1/3 items-center">
					<h1 class="w-full text-white text-center text-xl">ASK ME ANYTHING</h1>
					<div class="flex-col space-y-3 px-1 self-center">
						<div class="bg-black bg-opacity-75 rounded-xl text-white text-center py-2">
							“What are the benefits of using natural skincare products?”
						</div>
						<div class="bg-black bg-opacity-75 rounded-xl text-white text-center py-2">
							“Are your products suitable for sensitive skin”
						</div>
						<div class="bg-black bg-opacity-75 rounded-xl text-white text-center py-2">
							“Do you offer any products for anti-aging?”
						</div>
						<div class="bg-black bg-opacity-75 rounded-xl text-white text-center py-2">
							“Can you provide information about your sustainability practices?”
						</div>
					</div>
				</div>
				<div class="basis-1/3">
					<h1 class="w-full text-white text-center text-xl">DISCLAIMERS</h1>
					<div class="bg-black bg-opacity-75 rounded-xl text-white text-center">
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

			<div class="hidden md:flex md:flex-row w-3/4 justify-stretch self-center">
				<div class="basis-1/3">
					<h1 class="w-full text-white text-center text-xl">CAPABILITIES</h1>
					<div
						class="bg-black bg-opacity-75 rounded-xl text-white text-center hover:bg-opacity-90 py-2"
					>
						Remembers what user said earlier in the conversation
						<br />
						<br />
						Allows user to provide follow-up corrections
						<br />
						<br />
						Trained to decline inappropriate requests
					</div>
				</div>
				<div class="basis-1/3 items-center">
					<h1 class="w-full text-white text-center text-xl">ASK ME ANYTHING</h1>
					<div class="flex-col space-y-3 px-1 self-center">
						<div class="bg-black bg-opacity-75 rounded-xl text-white text-center py-2">
							“What are the benefits of using natural skincare products?”
						</div>
						<div class="bg-black bg-opacity-75 rounded-xl text-white text-center py-2">
							“Are your products suitable for sensitive skin”
						</div>
						<div class="bg-black bg-opacity-75 rounded-xl text-white text-center py-2">
							“Do you offer any products for anti-aging?”
						</div>
						<div class="bg-black bg-opacity-75 rounded-xl text-white text-center py-2">
							“Can you provide information about your sustainability practices?”
						</div>
					</div>
				</div>
				<div class="basis-1/3">
					<h1 class="w-full text-white text-center text-xl">DISCLAIMERS</h1>
					<div class="bg-black bg-opacity-75 rounded-xl text-white text-center">
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

			<div class="chat-message">
				<div class="flex items-end">
					<div class="flex flex-col space-y-2 text-xs max-w-xs mx-2 order-2 items-start">
						<div>
							<span
								class="px-4 py-2 rounded-lg inline-block rounded-bl-none bg-gray-300 text-gray-600"
								>Can be verified on any platform using docker</span
							>
						</div>
					</div>
					<img
						src="https://images.unsplash.com/photo-1549078642-b2ba4bda0cdb?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=facearea&amp;facepad=3&amp;w=144&amp;h=144"
						alt="My profile"
						class="w-6 h-6 rounded-full order-1"
					/>
				</div>
			</div>
			<div class="chat-message">
				<div class="flex items-end justify-end">
					<div class="flex flex-col space-y-2 text-xs max-w-xs mx-2 order-1 items-end">
						<div>
							<span
								class="px-4 py-2 rounded-lg inline-block rounded-br-none bg-green-900 text-white"
								>Your error message says permission denied, npm global installs must be given root
								privileges.</span
							>
						</div>
					</div>
					<img
						src="https://images.unsplash.com/photo-1590031905470-a1a1feacbb0b?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=facearea&amp;facepad=3&amp;w=144&amp;h=144"
						alt="My profile"
						class="w-6 h-6 rounded-full order-2"
					/>
				</div>
			</div>
			<div class="chat-message">
				<div class="flex items-end">
					<div class="flex flex-col space-y-2 text-xs max-w-xs mx-2 order-2 items-start">
						<div>
							<span class="px-4 py-2 rounded-lg inline-block bg-gray-300 text-gray-600"
								>Command was run with root privileges. I'm sure about that.</span
							>
						</div>
						<div>
							<span class="px-4 py-2 rounded-lg inline-block bg-gray-300 text-gray-600"
								>I've update the description so it's more obviously now</span
							>
						</div>
						<div>
							<span class="px-4 py-2 rounded-lg inline-block bg-gray-300 text-gray-600"
								>FYI https://askubuntu.com/a/700266/510172</span
							>
						</div>
						<div>
							<span
								class="px-4 py-2 rounded-lg inline-block rounded-bl-none bg-gray-300 text-gray-600"
							>
								Check the line above (it ends with a # so, I'm running it as root )
								<pre># npm install -g @vue/devtools</pre>
							</span>
						</div>
					</div>
					<img
						src="https://images.unsplash.com/photo-1549078642-b2ba4bda0cdb?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=facearea&amp;facepad=3&amp;w=144&amp;h=144"
						alt="My profile"
						class="w-6 h-6 rounded-full order-1"
					/>
				</div>
			</div>
			<div class="chat-message">
				<div class="flex items-end justify-end">
					<div class="flex flex-col space-y-2 text-xs max-w-xs mx-2 order-1 items-end">
						<div>
							<span
								class="px-4 py-2 rounded-lg inline-block rounded-br-none bg-green-900 text-white"
								>Any updates on this issue? I'm getting the same error when trying to install
								devtools. Thanks</span
							>
						</div>
					</div>
					<img
						src="https://images.unsplash.com/photo-1590031905470-a1a1feacbb0b?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=facearea&amp;facepad=3&amp;w=144&amp;h=144"
						alt="My profile"
						class="w-6 h-6 rounded-full order-2"
					/>
				</div>
			</div>
			<div class="chat-message">
				<div class="flex items-end">
					<div class="flex flex-col space-y-2 text-xs max-w-xs mx-2 order-2 items-start">
						<div>
							<span
								class="px-4 py-2 rounded-lg inline-block rounded-bl-none bg-gray-300 text-gray-600"
								>Thanks for your message David. I thought I'm alone with this issue. Please, ? the
								issue to support it :)</span
							>
						</div>
					</div>
					<img
						src="https://images.unsplash.com/photo-1549078642-b2ba4bda0cdb?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=facearea&amp;facepad=3&amp;w=144&amp;h=144"
						alt="My profile"
						class="w-6 h-6 rounded-full order-1"
					/>
				</div>
			</div>

			<div class="chat-message">
				<div class="flex items-end">
					<div class="flex flex-col space-y-2 text-xs max-w-xs mx-2 order-2 items-start">
						<div>
							<span class="px-4 py-2 rounded-lg inline-block bg-gray-300 text-gray-600"
								>It seems like you are from Mac OS world. There is no /Users/ folder on linux ?</span
							>
						</div>
						<div>
							<span
								class="px-4 py-2 rounded-lg inline-block rounded-bl-none bg-gray-300 text-gray-600"
								>I have no issue with any other packages installed with root permission globally.</span
							>
						</div>
					</div>
					<img
						src="https://images.unsplash.com/photo-1549078642-b2ba4bda0cdb?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=facearea&amp;facepad=3&amp;w=144&amp;h=144"
						alt="My profile"
						class="w-6 h-6 rounded-full order-1"
					/>
				</div>
			</div>
			<div class="chat-message">
				<div class="flex items-end justify-end">
					<div class="flex flex-col space-y-2 text-xs max-w-xs mx-2 order-1 items-end">
						<div>
							<span
								class="px-4 py-2 rounded-lg inline-block rounded-br-none bg-green-900 text-white"
								>yes, I have a mac. I never had issues with root permission as well, but this helped
								me to solve the problem</span
							>
						</div>
					</div>
					<img
						src="https://images.unsplash.com/photo-1590031905470-a1a1feacbb0b?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=facearea&amp;facepad=3&amp;w=144&amp;h=144"
						alt="My profile"
						class="w-6 h-6 rounded-full order-2"
					/>
				</div>
			</div>
			<div class="chat-message">
				<div class="flex items-end">
					<div class="flex flex-col space-y-2 text-xs max-w-xs mx-2 order-2 items-start">
						<div>
							<span class="px-4 py-2 rounded-lg inline-block bg-gray-300 text-gray-600"
								>I get the same error on Arch Linux (also with sudo)</span
							>
						</div>
						<div>
							<span class="px-4 py-2 rounded-lg inline-block bg-gray-300 text-gray-600"
								>I also have this issue, Here is what I was doing until now: #1076</span
							>
						</div>
						<div>
							<span
								class="px-4 py-2 rounded-lg inline-block rounded-bl-none bg-gray-300 text-gray-600"
								>even i am facing</span
							>
						</div>
					</div>
					<img
						src="https://images.unsplash.com/photo-1549078642-b2ba4bda0cdb?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=facearea&amp;facepad=3&amp;w=144&amp;h=144"
						alt="My profile"
						class="w-6 h-6 rounded-full order-1"
					/>
				</div>
			</div>
		</div>

		<div class="h-screen w-full flex flex-col bg-cover -z-20 bg-[url('/backgroundtrees.png')]">
			<div class="flex-none">
				<br /><br />
				<p class="lg:text-6xl flex justify-center text-white text-xl">ORIGINS ASSISTANT</p>
				<p class="lg:text-xl text-sm flex justify-center text-white">
					Powered by Artificial Intelligence Technology
				</p>
			</div>

			<div class="flex-grow overflow-y-auto">
				<div class="flex justify-items-center">
					<ChatBox />
				</div>
			</div>

			<div class="w-full py-3 px-5 h-20 flex-none inline-flex">
				<input
					class="w-full bg-gray-300 px-3 rounded-l-xl bottom-0"
					type="text"
					placeholder="type your message here..."
				/>

				<button
					class="bg-green-900 hover:bg-green-900 text-gray-800 font-bold py-2 px-4 rounded-r-xl inline-flex items-center"
				>
					<span class="text-white">Send</span>
				</button>
			</div>
		</div>
	</body>
</html>
