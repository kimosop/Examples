package com.peat.examples;

import org.json.simple.JSONObject;
import org.json.simple.JSONArray;
import org.json.simple.JSONValue;

import java.io.IOException;
import java.io.InputStream;
import java.io.StringWriter;
import java.net.URL;
import java.net.URLConnection;
import java.nio.charset.StandardCharsets;

import org.apache.commons.io.IOUtils;

public class DiseaseMinimal {
    public final static String baseUrl = "http://api.peat-cloud.com/diseases/";
    public final static String apiKey = "<YOUR_API_KEY>";

    public void sendJson(String plantName) {
        String charset = StandardCharsets.UTF_8.name();
        try {
            String url = baseUrl + plantName;
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
        String plantName = "tomato";
        DiseaseMinimal m = new DiseaseMinimal();
        m.sendJson(plantName);
    }

}
