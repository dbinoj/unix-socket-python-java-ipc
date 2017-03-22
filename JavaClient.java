import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

import com.etsy.net.*;

public class JavaClient {
	public static void main(String[] args) throws IOException, InterruptedException {
		if (args.length != 2) {
			System.out.println("usage: $java -cp juds/juds-0.95.jar: JavaClient <socketfilename> <yourname>");
			System.exit(1);
		}
		String socketFile = args[0];
		String username = args[1];

		long progStartTime = System.nanoTime();

		for (int itr = 0; itr < 10000; itr++) {


			UnixDomainSocketClient socket = new UnixDomainSocketClient(socketFile,
					JUDS.SOCK_STREAM);
			InputStream in = socket.getInputStream();
			OutputStream out = socket.getOutputStream();
			out.write(username.getBytes());
			String resp = "";
			for (int b = 0; ((b = in.read()) >= 0);) {
				resp += (char) b;
			}

			socket.close();
		}

		long progEndTime = System.nanoTime();
		System.out.println("Program runtime: " + 
				Long.toString(progEndTime - progStartTime));

	}
}
