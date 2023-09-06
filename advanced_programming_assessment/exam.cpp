#include <iostream>
#include <string>
#include <vector>
#include <numeric>
#include <iomanip>

// define ANSI escape codes for text colors
#define RESET   "\033[0m"
#define RED     "\033[31m"      /* Red */
#define GREEN   "\033[32m"      /* Green */
#define YELLOW  "\033[33m"      /* Yellow */
#define BLUE    "\033[34m"      /* Blue */
#define MAGENTA "\033[35m"      /* Magenta */
#define CYAN    "\033[36m"      /* Cyan */
#define WHITE   "\033[37m"      /* White */


//////////////////////////////////////////////////////////////////
// Function to sum 1st and last index and divide by middle index
//////////////////////////////////////////////////////////////////

float sum_first_last_divide_middle(std::vector<float> test_values) {
    if (test_values.size() < 2) {
        throw std::invalid_argument("This function requires a vector of at least two elements, edit in main() function where the vectors are held.");
 }
    float sum = test_values.front() + test_values.back();
    float middle;
    // If vector is even -1 division ti shift to lower index.
    if (test_values.size() % 2 == 0 ) {
    middle = test_values.at(test_values.size() / 2 -1); 
    
    }
    
    else
    {
    middle = test_values.at(test_values.size() / 2);
    }
    return sum / middle;
}

/////////////////////////////////////////////////////////////////
// Function to convert all positive numbers in a vector to negative
//////////////////////////////////////////////////////////////////

std::vector<float> as_negative(std::vector<float> inputVector) {
        if (inputVector.empty()) {
    throw std::invalid_argument("The inputVector should not be empty");
}
    
     
    // iterate over each element of the vector
    for (auto& i : inputVector) {
        // if the element is positive, make it negative
        if (i > 0) {
            i = -i;
        }
    }
    // return the updated vector
    return inputVector;
}

////////////////////////////////////////////////////////////////////
// Function to return a vector of the first n multiples of x
///////////////////////////////////////////////////////////////////
std::vector<int> n_multiples_of(int n, int x) {
    if (n <= 0 || x <= 0) {
        throw std::invalid_argument("n and x must be positive integers");
}
    std::vector<int> multiples;
    for (int i = 1; i <= n; i++) {
        multiples.push_back(i * x);
    }
    return multiples;
}

////////////////////////////////////////////////////////////////////
// is multiple function making use of numeric and reduction in 2017 C++ version
bool is_multiple(std::vector<int> number_set, int n) {
    if (number_set.empty()) {
    throw std::invalid_argument("The number_set should not be empty");
}
auto result = std::reduce(number_set.begin(), number_set.end());
     return result % n == 0; 
}




int main() {
    // The code in this function is provided as an example of how the
    // functions you write may be called. It is non-exhaustive and
    // does not check correctness.
    
    // First, last, middle calculation - testing different index sizes
    std::vector<float> test_values = {1, 4, 20, 11};
    std::vector<float> test_values2 = {1, 4, 25, 11, 49};
    std::vector<float> test_throw = {1};
    
try {
    float result = sum_first_last_divide_middle(test_values);
    std::cout << BLUE << "sum_first_last_divide_middle()" << RESET << std::endl;
    std::cout << "The sum of test_values, the first and last, divided by the middle element is " << result << std::endl;
    
    float result2 = sum_first_last_divide_middle(test_values2);
    std::cout << "The sum of test_values2, the first and last, divided by the middle element is " << result2 << std::endl;
    
    float result3 = sum_first_last_divide_middle(test_throw);
}   catch (const std::invalid_argument& e) {
    std::cerr << "Invalid argument: " << e.what() << std::endl;
}
    
    
//////////////////////////////////////////////////////////////////////    
     // As negative
    std::cout << std::endl;  // Just a blank line
    std::cout << BLUE << "as_negative()" << RESET << std::endl;
    std::vector<float> inputVector{-5.4, 4.0, 3.67};
    std::vector<float> negVector = as_negative(inputVector);
    for(auto i : negVector) {
        std::cout << std::fixed << std::setprecision(1) << i << " "; //sets precision
    }
    std::cout << std::endl;
     
////////////////////////////////////////////////////////////////////////
 
    // N multiples of
    std::cout << std::endl;  // Just a blank line
    int n = 5;
    int x = 4;
    std::vector<int> multiples = n_multiples_of(n, x);
    std::cout << BLUE << "n_multiples_of()" << RESET << std::endl;
    std::cout << "The " << n << " multiples of " << x << " are:" << std::endl;
    for (auto i : multiples) {
        std::cout << "  " << i << std::endl;
    }   

// Is multiple
    std::cout << std::endl;  // Just a blank line
    std::cout << BLUE << "is_multiple()" << RESET << std::endl;
    std::vector<int> number_set = {5, 9, 51, 4, 8, 95, 54, 96, 5}; //377 / 3 = 109
    auto multiple = 3;
    bool it_is_a_multiple = is_multiple(number_set, multiple);
    if(it_is_a_multiple) {
        std::cout << "Sum of list is a multiple of " << multiple << std::endl;
        std::cout << GREEN << "Success!" << RESET << std::endl;
    } else {
        std::cout << "Sum of list is not a multiple of " << multiple << std::endl;
        std::cout << RED << "Failure!" << RESET << std::endl;
    }
    
  
}

