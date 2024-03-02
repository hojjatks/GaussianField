# gpGenerator

Source code for generating 1D and 2D gaussian field using karhunen loeve expansion. 
# description
This code is written to generate 1D and 2D gaussian field. There are functions written in the code that find the eigen values and eigen functions of the covariance fucntion. To generate the gaussian random field one only needs to find the eigen function/values once. The covariance function is considered to be $exp(-\frac{1}{2}||x-y||^2)$. 

For example for 1D, we have:

$\int_a^b c(x,y)\phi(y)dy=\lambda \phi(x)$

Descritizing:
$\sum_i c(x_i,y_i)\phi(y_i)\Delta y=\lambda \phi(x_i)$

Then we write this as:
$A\phi=\lambda \phi$


## References

* [karhunen loeve expansion](https://en.wikipedia.org/wiki/Kosambi%E2%80%93Karhunen%E2%80%93Lo%C3%A8ve_theorem)
