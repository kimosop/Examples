package com.peat.examples;

import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

public class ImageAPIMinimal {
    private static final String API_KEY = "c735dc92e045233378013564d0eda4703e695efc";
    private static final String LINE_FEED = "\r\n";

    public static void main(String[] args) throws Exception {

        String charset = StandardCharsets.UTF_8.name();

        // Your image file to upload
        File uploadFile = new File("../../../python/data/tomato_nutrient/iron1.jpg");
        String requestURL = "http://api.peat-cloud.com/v1/image_analysis";

        // Creates a unique boundary based on time stamp
        String boundary = String.valueOf(System.currentTimeMillis());

        // Setup http connection
        URL url = new URL(requestURL);
        HttpURLConnection httpConn = (HttpURLConnection) url.openConnection();
        httpConn.setUseCaches(false);
        httpConn.setDoOutput(true); // POST method
        httpConn.setRequestProperty("User-Agent", "API Java example");
        httpConn.setRequestProperty("Content-Type", "multipart/form-data; boundary=" + boundary);
        httpConn.setRequestProperty("api_key", API_KEY);

        // Setup OutputStream and PrintWriter
        OutputStream outputStream = httpConn.getOutputStream();
        PrintWriter writer = new PrintWriter(new OutputStreamWriter(outputStream, charset), true);

        // Add image file to POST request
        String fieldName = "picture";
        String fileName = uploadFile.getName();
        writer.append("--" + boundary).append(LINE_FEED);
        writer.append("Content-Disposition: form-data; name=\"" + fieldName + "\"; filename=\"" + fileName + "\"").append(LINE_FEED);
        writer.append(LINE_FEED);
        writer.flush();

        FileInputStream inputStream = new FileInputStream(uploadFile);
        byte[] buffer = new byte[4096];
        int bytesRead;
        while ((bytesRead = inputStream.read(buffer)) != -1) {
            outputStream.write(buffer, 0, bytesRead);
        }
        outputStream.flush();
        inputStream.close();

        writer.append(LINE_FEED);
        writer.flush();

        // Send POST request and get response
        List<String> response = new ArrayList<>();
        writer.append(LINE_FEED).flush();
        writer.append("--" + boundary + "--").append(LINE_FEED);
        writer.close();

        // Check server status message
        int status = httpConn.getResponseCode();
        if (status == HttpURLConnection.HTTP_OK) {
            BufferedReader reader = new BufferedReader(new InputStreamReader(
                    httpConn.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                response.add(line);
            }
            reader.close();
            httpConn.disconnect();
        } else {
            throw new IOException("Server returned non-OK status: " + status);
        }

        // Read response
        for (String line : response) {
            System.out.println(line);
        }

    }
}
