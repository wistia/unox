class UnisonFsmonitor < Formula
  desc 'A layer for unison-fsmonitor around macfsevents for usage with unison'
  homepage 'https://github.com/wistia/unox'
  url 'https://codeload.github.com/wistia/unox/tar.gz/0.2.1'
  head 'https://github.com/wistia/unox.git', :using => :git, :revision => '0.2.1'
  sha256 'ab2c481401d7eba6cbbe9a3a4469a072a1e1b2e1fa43338f44e324f6a821130a'
  revision 1
  depends_on :python => :recommended if MacOS.version <= :snow_leopard
  depends_on :python3 => :optional

  resource "macfsevents" do 
    url "https://pypi.python.org/packages/f4/fb/59f72719e339f6209997414c6d0b7e1e1f96900dede3ec1cc24008471cc2/MacFSEvents-0.7.tar.gz"
    sha256 "95d3cddaf8a42435bfbd50087785ee9e3ebb8325242cfd06a88ea21f85bcb56f"
  end

  include Language::Python::Virtualenv

  def install
    virtualenv_install_with_resources
  end
end
