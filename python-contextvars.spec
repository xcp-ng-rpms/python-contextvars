# what it's called on pypi
%global srcname contextvars
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%bcond_without  tests

%global common_description %{expand:
This package implements a backport of Python 3.7 contextvars module (see PEP
567) for Python 3.6.}


Name:           python-%{pkgname}
Version:        2.4
Release:        1%{?dist}
Summary:        PEP 567 Backport
License:        ASL 2.0
URL:            https://github.com/MagicStack/contextvars
Source0:        %pypi_source
BuildArch:      noarch


%description %{common_description}


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-immutables
%endif


%description -n python3-%{pkgname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
%pytest --verbose
%endif


%files -n python3-%{pkgname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Apr 21 2021 Carl George <carl@george.computer> - 2.4-1
- Initial package rhbz#1951871
