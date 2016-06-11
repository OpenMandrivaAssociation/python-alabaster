# disable these for bootstrapping nose and sphinx
%bcond_with tests
%bcond_without python2

Summary:	Theme for the Sphinx documentation generator

Name:		python-alabaster
Version:	0.7.8
Release:	1
Source0:	https://pypi.python.org/packages/46/01/3539c406b47b0e44464a2b6c7b51871300d815b9d7b07c98309c9270bd50/alabaster-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://sphinx.pocoo.org/
BuildArch:	noarch
Requires:	python-pkg-resources
Requires:	python-docutils
Requires:	python-jinja2
Requires:	python-pygments
BuildRequires:	python-setuptools
%if %{with doc}
BuildRequires:	python-docutils >= 0.7
BuildRequires:	python-jinja2 >= 2.3
%endif
%if %{with tests}
BuildRequires:	python-nose
BuildRequires:	python-pygments
BuildRequires:  python-jinja2
%endif
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3-distribute
%rename python3-sphinx

%description
Alabaster is a visually (c)lean, responsive, configurable theme for the Sphinx
documentation system. It is Python 2+3 compatible.

It began as a third-party theme, and is still maintained separately, but as of
Sphinx 1.3, Alabaster is an install-time dependency of Sphinx and is selected
as the default theme.

Sphinx is a tool that facilitates the creation of beautiful
documentation for Python projects from reStructuredText sources. It
was originally created to format the new documentation for Python, but
has since been cleaned up in the hope that it will be useful in many
other projects.

%if %{with python2}
%package -n python2-alabaster
Summary:	Theme for the Sphinx documentation generator
Group:		Development/Python
Requires:	python2-docutils >= 0.7
Requires:	python2-pygments >= 1.2
Requires:	python2-jinja2 >= 2.3
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-nose
BuildRequires:	python2-pygments
BuildRequires:  python2-jinja2
BuildRequires:	python2-setuptools

%description -n python2-alabaster
Alabaster is a visually (c)lean, responsive, configurable theme for the Sphinx
documentation system. It is Python 2+3 compatible.

It began as a third-party theme, and is still maintained separately, but as of
Sphinx 1.3, Alabaster is an install-time dependency of Sphinx and is selected
as the default theme.

Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.
%endif

%prep
%setup -qc -b 0
mv alabaster-%{version} python3

%if %{with python2}
cp -r python3 python2
%endif

%build
%if %{with python2}
cd python2
python2 setup.py build
cd ..
%endif

cd python3
python setup.py build
cd ..

%install
%if %{with python2}
cd python2
python2 setup.py install --skip-build --root %{buildroot}
cd ..
%endif

cd python3
python setup.py install --skip-build --root=%{buildroot} 
cd ..

%check
%if %{with tests}
%if %{with python2}
cd python2/tests
python2 run.py
cd ../..
%endif
cd python3
make test
cd ..
%endif

%files
%{py_puresitedir}/*

%if %{with python2}
%files -n python2-alabaster
%{py2_puresitedir}/*
%endif