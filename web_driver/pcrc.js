var pcrc = {
	commands: {
		"#PLY": ()=>{console.warn("Play"); pcrc.send("OK");},
		"#VDN": ()=>{console.warn("Volume Down"); pcrc.send("OK");},
		"#VUP": ()=>{console.warn("Volume Up"); pcrc.send("OK");},
		"#NXT": ()=>{console.warn("Next"); pcrc.send("OK");},
		"#PRV": ()=>{console.warn("Previous"); pcrc.send("OK");},
		"#C01": ()=>{console.warn("Command 1"); pcrc.send("OK");},
		"#C02": ()=>{console.warn("Command 2"); pcrc.send("OK");},
		"#C03": ()=>{console.warn("Command 3"); pcrc.send("OK");},
		"#C04": ()=>{console.warn("Command 4"); pcrc.send("OK");},
		"#C05": ()=>{console.warn("Command 5"); pcrc.send("OK");},
		"#C06": ()=>{console.warn("Command 6"); pcrc.send("OK");},
		"#C07": ()=>{console.warn("Command 7"); pcrc.send("OK");},
		"#C08": ()=>{console.warn("Command 8"); pcrc.send("OK");},
		"#C09": ()=>{console.warn("Command 9"); pcrc.send("OK");},
		"#C10": ()=>{console.warn("Command 10"); pcrc.send("OK");},
		"#C11": ()=>{console.warn("Command 11"); pcrc.send("OK");},
		"#C12": ()=>{console.warn("Command 12"); pcrc.send("OK");}
	},
	port: null,
	reader: null,
	writer: null,
	time: null,
	encoder: new TextEncoder(),
	decoder: new TextDecoder(),
	connect: async (run_handler = true, run_timer = true) => {
		pcrc.port = await navigator.serial.requestPort();
		await pcrc.port.open({ baudRate: 9600 });
		pcrc.reader = pcrc.port.readable.getReader();
		pcrc.writer = pcrc.port.writable.getWriter();
		setTimeout((run_handler, run_timer) => {
		    if(run_handler){
			    pcrc.handler();
		    };
		    if(run_timer){
			    pcrc.timer();
		    };
		}, 3000, run_handler, run_timer);
	},
	handler: async () => {
		while(true){
			let raw_command = (await pcrc.reader.read()).value.buffer;
			let command = pcrc.decoder.decode(raw_command).replace("\r\n","");
			pcrc.commands[command]();
		};
	},
	timer: () => {
	    setInterval(() => {
	        let date = new Date();
	        let time = String(date.getHours()).padStart(2,"0") + String(date.getMinutes()).padStart(2,"0");
	        if(time != pcrc.time){
	            pcrc.time = time;
	            pcrc.send(time);
	        }
	    }, 1000);
	},
	send: async (text) => {
		await pcrc.writer.write(pcrc.encoder.encode(text));
	}
};
