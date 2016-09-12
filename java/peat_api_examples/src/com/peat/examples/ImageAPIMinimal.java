package com.peat.examples;

import org.json.simple.JSONObject;
import org.json.simple.JSONArray;
import org.json.simple.JSONValue;

import java.awt.image.BufferedImage;
import java.io.*;
import java.net.URL;
import java.net.URLConnection;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

import org.apache.commons.io.IOUtils;

import javax.imageio.ImageIO;

public class ImageAPIMinimal {
    public final static String baseUrl = "http://api.plantix.net/v1/image_analysis";
    public final static String apiKey = "<YOUR_API_KEY";

    private String processImage(String pathToImage, String charset) {
        String encodedImage = "";
        try {
            BufferedImage img = ImageIO.read(new File(pathToImage));
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ImageIO.write(img, "jpg", baos);
            baos.flush();
            Base64.Encoder base = Base64.getEncoder();
            encodedImage = base.encodeToString(baos.toByteArray());
            baos.close();
            encodedImage = java.net.URLEncoder.encode(encodedImage, charset);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return encodedImage;
    }

    private String readJSON(String pathToJSON) {
        String result = "";
        try {
            BufferedReader bfreader = new BufferedReader(new FileReader(new File(pathToJSON)));
            result = bfreader.readLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return result;
    }

    public void sendJson(String pathToImage, String pathToJSON) {
        String charset = StandardCharsets.UTF_8.name();
        String image = this.processImage(pathToImage, charset);
        String reqJson = this.readJSON(pathToJSON);
        try {
            String url = baseUrl + "?picture=" + image + "?json=" + reqJson;
            URLConnection connection = new URL(url).openConnection();
            connection.setRequestProperty("api_key", apiKey);
            connection.setRequestProperty("Accept-Charset", charset);
            InputStream response = connection.getInputStream();

            StringWriter respBuffer = new StringWriter();
            IOUtils.copy(response, respBuffer, charset);
            JSONObject jsonResponse = (JSONObject) JSONValue.parse(respBuffer.toString());
            // get the status code
            System.out.println(jsonResponse.get("code"));
            // get the data
            JSONArray diseases = (JSONArray) jsonResponse.get("data");
            System.out.println(diseases.size());

            for(Object json: diseases) {
                JSONObject jsonObject = (JSONObject) json;
                for(Object key  : jsonObject.keySet()) {
                    StringBuilder strBuild = new StringBuilder("\t");
                    strBuild.append(key);
                    strBuild.append("\n");
                    strBuild.append("\t\t");
                    strBuild.append(jsonObject.get(key));
                    System.out.println(strBuild.toString());
                }
                System.out.println("\n\n\n");
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        String pathToImage = "../python/data/iron1.jpg";
        String pathToJSON = "../python/data/example.json";
        ImageAPIMinimal m = new ImageAPIMinimal();
        m.sendJson(pathToImage, pathToJSON);
    }
}
