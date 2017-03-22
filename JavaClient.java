import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

import com.etsy.net.*;

public class JavaClient {
	public static void main(String[] args) throws IOException, InterruptedException {
		if (args.length != 1) {
			System.out.println("usage: $java -cp juds/juds-0.95.jar: Test <socketfilename>");
			System.exit(1);
		}
		String socketFile = args[0];

		for (int itr = 0; itr < 100; itr++) {
			long socStartTime = System.nanoTime();


			UnixDomainSocketClient socket = new UnixDomainSocketClient(socketFile,
					JUDS.SOCK_STREAM);
			long socEndTime = System.nanoTime();
			InputStream in = socket.getInputStream();
			OutputStream out = socket.getOutputStream();
			long startTime = System.nanoTime();
			String text = "Java";
			out.write(text.getBytes());
			String resp = "";
			for (int b = 0; ((b = in.read()) >= 0);) {
				resp += (char) b;
			}
			long endTime = System.nanoTime();

			socket.close();

			System.out.println(resp);
			System.out.println("Nanoseconds to open socket                 : " + 
					Long.toString(socEndTime - socStartTime));
			System.out.println("Nanoseconds to send, process & receive data: " + 
					Long.toString(endTime - startTime));
		}

	}
}
