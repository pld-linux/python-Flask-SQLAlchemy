#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	Flask-SQLAlchemy
Summary:	Adds SQLAlchemy support to your Flask application
Name:		python-%{module}
Version:	0.15
Release:	0.1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/F/Flask-SQLAlchemy/%{module}-%{version}.tar.gz
# Source0-md5:	d69571aee51eec584b0978c35ca047ba
#URL:		-
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-Flask
Requires:	python-SQLAlchemy
Requires:	python-modules
Requires:	python-setuptools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Adds SQLAlchemy support to your Flask application.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{py_sitescriptdir}/flaskext
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/Flask_SQLAlchemy-*.egg-info
%endif
