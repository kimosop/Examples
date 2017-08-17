#include <cstdlib>
#include <cstdio>
#include <cstring>

#include <boost/format.hpp>

#include <sstream>

#include <curlpp/cURLpp.hpp>
#include <curlpp/Easy.hpp>
#include <curlpp/Options.hpp>
#include <curlpp/Exception.hpp>

const std::string API_KEY = "<YOUR_API_KEY>";
const std::string LANGUAGE = "en";
const std::string PLANT_NAME = "TOMATO";
int main(int argc, char *argv[]) {

    std::string url = str(boost::format("http://api.peat-cloud.com/diseases/%1%/%2%") % PLANT_NAME % LANGUAGE);

    try {
        curlpp::Cleanup cleaner;
        curlpp::Easy request;

        std::list<std::string> headers;
        headers.push_back("Content-Type: text/*");
        std::string api_str = str(boost::format("api_key: %1%") % API_KEY);
        headers.push_back(api_str);

        using namespace curlpp::Options;
        request.setOpt(new Verbose(true));
        request.setOpt(new HttpHeader(headers));
        request.setOpt(new Url(url.c_str()));

        std::ostringstream os;
        request.setOpt(new WriteStream(&os));

        request.perform();

        os << request;

        std::cout << os.str() << std::endl;
    }
    catch (curlpp::LogicError & e) {
        std::cout << e.what() << std::endl;
    }
    catch (curlpp::RuntimeError & e) {
        std::cout << e.what() << std::endl;
    }
    return 0;
}