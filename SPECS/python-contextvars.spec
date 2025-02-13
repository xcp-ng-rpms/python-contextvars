%global package_speccommit 778f2f91bf091e588d4fd549925904ef2791c72b
%global usver 2.4
%global xsver 3
%global xsrel %{xsver}.1%{?xscount}%{?xshash}
# what it's called on pypi
%global srcname contextvars
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%bcond_with tests

%global common_description %{expand:
This package implements a backport of Python 3.7 contextvars module (see PEP
567) for Python 3.6.}


Name:           python-%{pkgname}
Version:        2.4
Release:        %{?xsrel}%{?dist}
Summary:        PEP 567 Backport
License:        ASL 2.0
URL:            https://github.com/MagicStack/contextvars
Source0: contextvars-2.4.tar.gz
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

Requires:       python3-immutables

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
* Fri Jan 24 2025 Yann Dirson <yann.dirson@vates.tech> - 2.4-3.1
- Add missing Requires: python3-immutables

* Mon Aug 19 2024 Marcus Granado <marcus.granado@cloud.com> - 2.4-3
- Bump release and rebuild

* Fri Aug 09 2024 Marcus Granado <marcus.granado@cloud.com> - 2.4-3
- Bump release and rebuild

* Fri Feb 16 2024 Rachel Yan <rachel.yan@citrix.com> - 2.4-1
- Initial import
