<h1> Reproducible research software </h1>
It is important for scientific research that computational analysis are reproducible: that the code and data are assembled in a way so that someone else can re-create all of the results. Here, someone else can be a different research group but also a different person in your own research group. Furthermore, it is beneficial for your own work if you can re-create your analysis.

<h3> Factors that make software/analsyis irreproducible </h3>
There are a number of factors that make your analysis not reproducible:
<ul>
  <li>Not enough (or no) documentation on how the experiment is conducted and data is obtained.</li>
  <li>Data to generate the results is not available.</li>
  <li>Software used to generate results is unavailable</li>
  <li>Difficult to recreate software environment</li>
  <li>Difficult to rerun the analysis</li>
</ul>
<br>
In this section we will mainly discuss the reproducibility of research code (Data documentation is discussed in another section). We will have a look into best practices, the available solutions, and so on. You can also download the powerpoint presentation in this repository to learn more about reproducibile research software.

<h3> Software version control </h3>
When you are working in a computational group, you can benefit from using version control software such as git. Version control keeps track of every modification to the code and allows programmers to return to a previous version if a major error occures. Furthermore, repositories such as GitHub or Gitlab can help you share your research code with the world. <br>
<h4> What is GitHub </h4>
Github is a commercial version-control hosting platform that offers a web interface and provides a mixture of both free and paid served for working with repositories. THe web interface offers a straightforward way to share your porjects online with colleagues and other researchers. It is useful for you as a researcher, as it allows you to find, develop, and publish scripts and research software. <br>
<h4> Create a repository on GitHub </h4>
When creating a repositories, there are a couple of things to think about. First, give the repository a name that makes sense to you and others. For example, when you develop a new tool, give the repository the name of that tool. Second, do you already want to make your repository public or would you like to work in a private environment? A private environment allows you to make full use of the version control but third parties cannot see your work.

<h3> Software licenses </h3>
Although you might not worry too much about a license, it is actually vital to pick one:
<i>Even in the absence of a license file, you may grant some rights in cases where you publish your source code to a site that requires accepting terms of service. For example, if you publish your source code in a public repository on GitHub, you have accepted the Terms of Service, by which you allow others to view and fork your repository. Others may not need your permission if limitations and exceptions to copyright apply to their particular situation. https://choosealicense.com </i>
<br />
Like Research Data licenses, there are special licenses for research software: the <b>FOSS</b> license. <br/>
<h5> The FOSS license </h5>
The primary goal of the FOSS license is to maximize openness and minimize barriers to (re)use software. When you pick a Free and Open Source license, you have a wide variety of licenses to choose from. Each of the licenses vary in some important ways, but the all grant free, open, and non-discriminatory access and rights to modify licensed software and associated source code. For a detailed version of the license and copyright notice, visit <a href='https://choosealicense.com/licenses/'>Choose a license</a>.
<br>

