Fonksiyon ve metotlar çağrılabilirdir. __call__() özel metodu ile herhangi bir nesneye çağırma işlemi uygulanabilir.
Bir decorator’de çağrılabilen bir nesnedir ve temel olarak bir decorator bir fonksiyonu alır, yeni fonksiyonellikler ekler ve döndürür.
Dİğer bir değişle, fonksiyonun yapısını değiştirmeden çalışma şeklini değiştirerek kontrol etmek için kullanılırlar.

Pytest Decorator'lerinden bazıları ve bunların işlevleri aşağıdaki gibidir:

	* @pytest.mark.paramaterize(): Fonksiyon'u test ederken belirlenen giriş parametrelerini ana test döngüsünden çıkmadan test edilmesini sağlayan decoratordür.
	
	* @pytest.mark.skip(): Test sırasında belirli bir fonksiyonun testinin geçici olarak atlanmasına olanak sağlar. 
	
	* @pytest.mark.skipif(): Belirli bir koşula bağlı olarak bir fonksiyonun testinin geçici olarak atlanmasını sağlar.
	
	* @pytest. mark.xfail(): Skip'ten farklı olarak, test döndürülür fakat ilgili fonksiyon hatalar arasında sayılmaz.
	
	* @pytest.fixture(): Testlerde ihtiyaç olacak veriler oluşturmak için kullanılır. Aynı zamanda tekrar eden kodları engelleyerek kod düzenini sağlar.
	
	* @pytest.mark.order(): Testlerin sırasını belirlemek için kullanılır.
	
	