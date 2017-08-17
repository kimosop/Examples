cmake_minimum_required(VERSION 2.8)

project(peat_api_examples)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON) 

set(CURLPP_LIBRARY /usr/lib/x86_64-linux-gnu/libcurlpp.so)
set(CURL_LIBRARY /usr/lib/x86_64-linux-gnu/libcurl.so)

add_executable(disease_minimal src/disease_minimal.cpp)

add_executable(symptoms_minimal src/symptoms_minimal.cpp)

#add_executable(image_minimal src/image_minimal.cpp)

target_link_libraries(disease_minimal
    ${CURL_LIBRARY}
    ${CURLPP_LIBRARY}
)

target_link_libraries(symptoms_minimal
    ${CURL_LIBRARY}
    ${CURLPP_LIBRARY}
)

#target_link_libraries(image_minimal
#    ${CURL_LIBRARY}
#    ${CURLPP_LIBRARY}
#)