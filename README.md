# PyBDS

Git Activity for Colloidal Physics Graduates.

## Create your own PyBDS Repository in GitHub

To create your own (public) PyBDS GitHub repository please follow the steps shown in our
online session. Feel free to consult GitHub's [documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository#creating-a-new-repository-from-the-web-ui) to create the repository with the web User Interface UI.

## Clone your own PyBDS Repository

After creating the repository you can now clone it in your local machine to develop your
own implementation of PyBDS.

Open up a terminal and clone your own PyBDS repository, the command line is going to be
similar to the following:

```sh
git clone git@github.com:{YOUR_GITHUB_USERNAME}/PyBDS.git
```

you will need to replace `{YOUR_GITHUB_USERNAME}` with your GitHub's username remember to exclude the braces `{}`, for example, in my case I would clone this repository with this
command `git clone git@github.com:misael-diaz/PyBDS.git`. Note that if you choose another
name for your repository (something other than `PyBDS`) you will need to account for
that as well.

## Your First Pull Request

In this section I am going to guide through the steps of creating your first pull
request.

What we are going to do in this section is just to add the general information
of the Brownian Dynamics Simulator BDS. (In practice you would add more than just
that in a pull-request but let's keep things simple while we are learning.)

Create the `synopsis` branch via:

```sh
git switch -c synopsis
```

Add the synopsis to the source `main.py` with your favorite text editor or IDE.

Once you are done with that stage those changes to the `synopsis` branch via:

```sh
git add main.py
```

And commit the changes to the branch via:

```sh
git commit
```

Add a brief but meaningful commit message, you may choose to add more in some other
commits as you can see in the commit history of this repository.

Push the changes to the upstream so that these will be visible in the GitHub repository:

```sh
git push origin HEAD
```

Create a pull request, add more comments if needed, and merge the changes into the
main branch (or master branch depending on the configuration that you have chosen).

Congratulations you have just merged your first pull request!

That's all you have to do until our next online meeting.
