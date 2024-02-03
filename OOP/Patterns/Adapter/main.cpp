#include <iostream>
#include <memory>

using namespace std;

class Adapter
{
    public:
        virtual ~Adapter() = default;
        virtual void request() = 0;
};

class BaseAdaptee
{
    public:
        virtual ~BaseAdaptee() = default;
        virtual void specificRequest() = 0;
};

class ConAdapter : public Adapter
{
    private:
        shared_ptr<BaseAdaptee> adaptee;
    public:
        ConAdapter(shared_ptr<BaseAdaptee> ad) : adaptee(ad) {}
        virtual void request() override;
};

class ConAdaptee : public BaseAdaptee
{
    public:
        virtual void specificRequest() override {cout << "Method ConAdaptee;" << endl;}
};

void ConAdapter::request()
{
    cout << "Adapter: ";
    if (adaptee)
    {
        adaptee->specificRequest();
    }
    else 
    {
        cout << "Empty!" << endl;
    }
};

int main()
{
    shared_ptr<BaseAdaptee> adaptee = make_shared<ConAdaptee>();
    shared_ptr<Adapter> adapter = make_shared<ConAdapter>(adaptee);

    adapter->request();
    return 0;
}